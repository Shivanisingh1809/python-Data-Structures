s=input()
d=0
u=0
l=0
for i in s:
    if i>='A' and i<='Z':
        u+=1
    elif i>='a' and i<='z':
        l+=1
    else:
        d+=1
a=list(s)
a.sort()
dt=a[:d]
do=[]
de=[]
for i in dt:
    if int(i)%2==0:
        de.append(i)
    else:
        do.append(i)
f=a[d+u:]+a[d:d+u]+do+de
print(''.join(map(str,f)))
