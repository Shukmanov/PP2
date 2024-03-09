n = int(input("Your n number: "))

square_generator = (sq ** 2 for sq in range(0, n))

for i in square_generator:
    print(i)


######

start = 1

def fib_generator():
    for i in range(0,n):
        i, ii = ii, i + ii
        yield i, ii

for i in fib_generator():
    print(i)