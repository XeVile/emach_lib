import math, cmath

# Use IEEE equivalent circuit of each arm of stator
def calc_I(V, Xm, R1=0, R2 = 0, X1 = 0, X2 = 0, S = 1):
    Rs = R1 + R2/S
    Xs = X1 + X2
    Im = V/(Xm*1j)
    I2_ = V/(Rs + Xs*1j)
    I1 = Im + I2_

    for (i, x) in {"Im": Im, "I2'": I2_, "I1": I1}.items():
        r, rad_arg = cmath.polar(x)
        deg_arg = math.degrees(rad_arg)
        print(f"\n{i} = {r:.3f}\u2220{deg_arg:.3f}")

    return Im, I2_, I1

# Torque at Slip Percentage (S)
calc_T = lambda I2_, R2, Ws, S = 1: (3*abs(I2_)**2 * R2/S)/Ws

# Slip calculation
calc_S = lambda Ns, Nr: (Ns - Nr)/Ns

# Power
calc_P_In = lambda V, I, pf: 3*V*abs(I)*pf
calc_P_Out = lambda T, Ws, S, P_rot: ((T * Ws)*(1 - S)) - P_rot