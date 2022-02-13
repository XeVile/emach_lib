import math

angle = lambda pf: math.degrees(math.acos(pf)) # Angle in respect real axis
pf = lambda arg: math.cos(math.radians(arg)) # Power factor
V_l2p = lambda V: V/math.sqrt(3) # Line voltage to phase converter
Ns = lambda f, poles: (120*f)/4 # Sync speed
Ws = Ns(50, 4) * (2*math.pi/60) # Speed In rpm