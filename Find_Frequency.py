# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:02:28 2023

@author: ellio
"""
import numpy as np


def doCalc(E,D,L):
    d = 0.003 # depth [m]
    b = 0.02 # breadth [m]
    I = (b*d**3)/12

    # finding the first undampened natural frequency
    w1 = (1.875)**2*np.sqrt((E*I)/((b*d)*D*L**4))
    w1Hz = w1/(2*3.14) # Convert from [rad/s] to Hz
    print(w1Hz/1000,"GHz")

def findHz(E,D):
    d = 0.003 # depth [m]
    b = 0.01 # breadth [m]
    I = (b*d**3)/12
    
    
    L = 0.5 # length [m]
    sl = 0.000001 # step length (decrease for better accuracy)
    while True:
        # finding the first undampened natural frequency in GHz
        w1 = (1.875)**2*np.sqrt((E*I)/((b*d)*D*L**4)) #formel
        w1GHz = (w1/(2*3.14))/1000 # Convert from [rad/s] to GHz
        if w1GHz <= 160:
            L=L-sl
        elif w1GHz > 160:
            w1 = (1.875)**2*np.sqrt((E*I)/((b*d)*D*L**4))
            w1GHz = (w1/(2*3.14))/1000 # Convert from [rad/s] to GHz
            print("found length",L, "m with a first undampened frequency of",w1GHz,"GHz")
            break

"""
#steel A36
E = 2.1*10**11 # modulus of the beam material [N/m^2]
D = 7850 # density [kg/m^3]
L = 0.003958# beam length [m] 0.3958 cm
"""

"""
# Molybdenum (annealed)
E = 3.3*10**11 # modulus of the beam material [N/m^2]
D = 10280 # density [kg/m^3]
L = 0.004143# beam length [m] 0.4143 cm
"""

"""
#Tungsten carbide
E = 6.0*10**11 # modulus of the beam material [N/m^2]
D = 15600 # density [kg/m^3]
L = 0.004334# beam length [m] 0.4334cm
"""

"""
#diamond(synthetic)
E = 1.05*10**12 # modulus of the beam material [N/m^2]
D = 3500 # density [kg/m^3]
L = 0.007243# beam length [m] 0.7343 cm
"""

# doCalc(E, D, L)

findHz(1.05*10**12, 3500)










