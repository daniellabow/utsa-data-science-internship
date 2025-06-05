# def countdown(n):
#    while n >= 0:
#        print(n)
#        n -= 1

# def countdown1(n):
#    print(n)
#    if n > 0:
#        countdown1(n-1)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()


fib(1000)
