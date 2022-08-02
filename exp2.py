n=input('enter any string : ')
let=0
vo=0
for i in n :
    let+=1
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vo+=1

print('no of vowels in the string is : ',vo)
print('percentage of vowels in the string is : ',(vo/let)*100)
