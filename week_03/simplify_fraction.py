
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def simpl_fraction(fraction):
    if not isinstance(fraction,tuple):
        raise ValueError('Not a tuple')
    if fraction[1]==0:
        raise ZeroDivisionError('Divison by zero!')
    if fraction[0]==fraction[1]:
        return (1,1)
    while gcd(max(fraction),min(fraction))>1:
        fraction=(fraction[0]/gcd(max(fraction),min(fraction)),fraction[1]/gcd(max(fraction),min(fraction)))

    return fraction

def sum_fractions(fractions):
    final_fract=fractions[0]
    for fraction in fractions[1:]:
        final_fract=(final_fract[0]*fraction[1]+fraction[0]*final_fract[1],final_fract[1]*fraction[1])
        final_fract=simpl_fraction(final_fract)
    return final_fract

def sort_fractions(fractions):
    fractions.sort(key=lambda x: x[0]/x[1])
    return fractions

