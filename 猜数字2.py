import random
a = random.randint(1,100)
b = int(input('请猜一个1~100的整数'))
while b!=a:
    if b>a :
        print('大了')
    elif b<a :
        print('小了')
    b=int(input('搞错了，再来！'))
print('猜对了~')