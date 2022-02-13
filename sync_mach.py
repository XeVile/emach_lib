import math, cmath
import conv

# Armature current
def calc_Ia(Ef = None, Xs = None, S = None, pf = None, Vt = None) -> complex:
    '''Returns the Armature current (Complex form) using the formula:\n 
    S3p = 3 * Vt * conj(Ia) \n
    OR \n
    Ia = (Ef - Vt)/Xs \n
    Use 2nd formula for Ques B \n
        \tWhere S3p = S\u2220arg \n
        * Note:\n
        \t* Vt is Line voltage\n
        \t* Xs is the reactance value\n
        * Units:\n
        \t* Ef: V\n
        \t* Xs: reactance\n
        \t* S: VA\n
        \t* arg: degrees\n
        \t* Vt: V'''
    if pf != None:
        arg = conv.angle(pf)
    if S != None:
        Ia = (cmath.rect(S,math.radians(arg)))/(3*Vt)
        r, rad_arg = cmath.polar(Ia)
        deg_arg = math.degrees(rad_arg)
        print(f"\nIa Conjugate = {r:.3f}\u2220{deg_arg:.3f}")
        print(f"\nIa= {r:.3f}\u2220{-deg_arg:.3f}")
        return Ia.conjugate()
    elif Ef != None:
        Ia = (Ef - Vt)/(1j*Xs)
        r, rad_arg = cmath.polar(Ia)
        deg_arg = math.degrees(rad_arg)
        print(f"\nIa= {r:.3f}\u2220{deg_arg:.3f}")
        return Ia

# Excitation Voltage
def calc_Ef(Ia, Xs, Vt) -> complex:
    '''Returns the Excitation Voltage (Complex form) using the formula:\n 
    Ef = Ia * Xs + Vt \n
        * Note:\n
        \t* Ia is complex form\n
        \t* Xs is the reactance value\n
        \t* Vt is Line voltage\n
        * Units:\n
        \t* Ia: A\n
        \t* Xs: reactance\n
        \t* Vt: V'''
    Ef = Ia*Xs*1j + Vt
    r, rad_arg = cmath.polar(Ef)
    deg_arg = math.degrees(rad_arg)
    print(f"\nEf = {r:.3f}\u2220{deg_arg:.3f}")
    return Ef

# On field current increase -> Find new Excitation voltage
# For QUESTION B
def increased_Ef(Ef, percent) -> complex:
    '''Returns the increased Excitation Voltage (Complex form) using the formula:\n 
    Ef' = Ef * (100+percent)/100 \n
    then\n
    arg' = asin(mag(Ef)*sin(arg)/Ef')\n
        * Note:\n
        \t* Ef is complex form\n
        * Units:\n
        \t* Ef: V\n
        \t* Percent: without %'''
    r, rad_arg= cmath.polar(Ef)
    Ef = abs(Ef)*(1 + percent/100)
    new_arg = math.asin(r*math.sin(rad_arg)/Ef)
    deg_arg = math.degrees(new_arg)
    print(f"\nEf = {Ef:.3f}\u2220{deg_arg:.3f}")
    return cmath.rect(Ef, new_arg)

# Calculate real and reactive Power
def calc_S(Vt, Ia) -> complex:
    '''Return the VA in complex form using formula:\n
    S3p = 3*Vt*conj(Ia)
    * Note:\n
        \t* Vt is Line voltage\n
    '''
    Ia_conj = Ia.conjugate()
    S = 3 * Vt * Ia_conj
    print(f"\nS = {S}")
    return S

# Max Power
def calc_Pmax(Vt, Ef, Xs) -> float:
    '''Returns the maximum Power in Watt using formula:\n
    At max power the angle is 90 degrees\n
    Pmax = (3 * mag(Vt) * mag(Ef) * sin(90)) / mag(Xs)\n
        * Note:\n
        \t* Vt is Line voltage\n
        \t* Ef is complex form\n
        \t* Xs is the reactance value\n'''
    Pmax = (3*Vt*abs(Ef))/Xs
    print(f"Pmax = {Pmax}")
    return Pmax

# Max Torque
def calc_Tmax(Pmax, frequency, poles) -> float:
    Tmax = Pmax/((120*frequency)/poles * ((2*math.pi)/60))
    print(f"Tmax = {Tmax} Nm")
    return Tmax