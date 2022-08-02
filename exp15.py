def minmax():
    n=int(input('enter range : '))
    l=[]
    for i in range(n):
        k=int(input('enter a number :'))
        l.append(k)
    max=0
    min=100
    for i in l:
        if i>max:
            max=i
        if i<min:
            min=i
    print('max num is : ',max)
    print('min num is : ',min)
minmax()
