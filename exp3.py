from collections import Counter
f1=open('Z:\\python\\spjans.txt','r')
t=f1.read().split()
print('the most common word is : ')
print(Counter(t).most_common(1))
