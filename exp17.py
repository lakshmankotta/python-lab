def binary(k):
    if k==0:
        return 0
    else :
        return k%2 +10 * binary(k//2)
n=int(input('enter a number'))
print('binary number is : ',binary(n))
