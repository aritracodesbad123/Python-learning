def fibonacci_generator(n):
    a,b =0,1
    for i in range(n):
        yield a
        a,b=b,a+b

for i in fibonacci_generator(7):
    print(i)
        




