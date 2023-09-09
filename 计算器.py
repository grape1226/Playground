a,f,b = input().split()
a = int(a)
b = int(b)
print('=',end=' ')
if f == '+':
    print(a+b)
elif f == '-':
    print(a-b)
elif f =='*':
    print(a*b)
else:
    print(a/b)