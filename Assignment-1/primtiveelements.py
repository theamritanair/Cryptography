import math


def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


def primitive_elements(a, outfile):
    for i in range(a+1):
        if(gcd(i,a)==1):
            outfile.write(str(i) + " ")
    print()
# primitive_elements(39877)
with open('output.txt', 'w+') as f:
    primitive_elements(39877, outfile = f)
with open('output1.txt', 'w+') as f:
    primitive_elements(31319, outfile = f)
with open('output3.txt', 'w+') as f:
    primitive_elements(39869, outfile = f)
    print()      
   