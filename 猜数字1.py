import random
a = random.randint(1, 100)
b = int(input('请猜一个1~100的整数'))
while True:
    if b > a:
        print('大了')
        b = int(input('再猜'))
    elif b < a:
        print('小了')
        b = int(input('再猜'))                                                                                                                    
    else:
        print('猜对了~')
        break