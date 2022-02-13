import sync_mach as q4
import ind_motor as q3
import conv
import math

# test calc from Eg
a = q4.increased_Ef(4776.3-099.423j, 10)

print(a)
c = q4.calc_Ia(Ef =a,Xs =20, Vt = conv.V_l2p(11000))
print(c)

# Test calc from Example
Im, I2_, I1 = q3.calc_I(415, 25, 0.3, 0.4, 0.5, 0.8, 1)
T_st = q3.calc_T(I2_, 0.4, conv.Ws)
S = q3.calc_S(conv.Ns(50, 4), 1455)
int_eff = 1 - S

_, I2_n, I1_n = q3.calc_I(415, 25, 0.3, 0.4, 0.5, 0.8, S)

I_eff = abs(I1*math.sqrt(3))/abs(I1_n*math.sqrt(3))

T_mech = q3.calc_T(I2_n, 0.4, conv.Ws, S)
P_eff = q3.calc_P_Out(T_mech, conv.Ws, S, 500)/q3.calc_P_In(415, I1_n*math.sqrt(3), conv.pf(32.848))

print(f"\nT_st = {T_st:.3f} Nm \n\nS = {S} \n\nRatio of current is {I_eff:.3f}\n\nDuring FL, T = {T_mech:0.3f}")
print(f" P_eff = {P_eff:.03f}")