a=int(input('enter anum : '))
b=int(input('enter anum : '))
for i in range(1,a+1):
    if a%i==0 and b%i==0 :
        hcf=i
lcm=int(a*b)//hcf
print('lcm is : ',lcm)
