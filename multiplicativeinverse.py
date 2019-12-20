import math

def extended_euclidean(a, b):
    s,old_s = 0,1
    t = 1
    old_t = 0
    if(a<b):
        r = a
        old_r =b
    else:
        r = b
        old_r = a

    while not(r==0):
        q = math.floor(old_r/r)
        old_r, r = r, old_r - (q*r)
        old_s, s = s, old_s - (q*s)
        old_t, t = t, old_t - (q*t)
        print(q)
        print("old_r, r" , old_r , r)
        print("old_s, s" , old_s , s)        
        print("old_t, t" , old_t , t)

    print("the multiplicative inverse is", old_t)

extended_euclidean(53947, 56211)
extended_euclidean(19385, 43159)