a = [7,8,9,2,3,1,4,10,6]
print(a)

b=a.copy()
b.sort()
print(b)

c=a.copy()
c.sort(reverse=True)
print(c)

d=a[::2]
print(d)

e=a[1::2]
print(e)

for i in range(0,len(a)):
    if a[i]%3==0:
        print(a[i])