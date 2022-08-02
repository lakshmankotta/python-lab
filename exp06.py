import cmath
a=int(input('enter x^2 coeff : '))
b=int(input('enter x coeff : '))
c=int(input('enter constant : '))
d= (b**2)-(4*a*c)
sol1=(-b +cmath.sqrt(d))/(2*a)
sol2=(-b -cmath.sqrt(d))/(2*a)
print('solutions are : ',sol1,sol2)
