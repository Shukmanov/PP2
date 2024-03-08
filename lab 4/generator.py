# ex1

n = int(input("type your number: "))
sq_generator = (sq ** 2 for sq in range(n))

for square in sq_generator:
    print(square)

# ex2

N = int(input("type your number: "))

even_num_generator = (even for even in range(N) if even % 2 == 0)
"""""(even if even % 2 == 0 else None for even in range(N)) """

for even_num in even_num_generator:
    print(even_num)
"""
even_num_generator = (even for even in range(N))

for even_num in even_num_generator:
    if even_num %2 == 0:
        print(even_num)
"""

# ex 3
div = int(input("type your div number: "))

def not_div_three_four():
    for i in range(div):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for div_num in not_div_three_four():
    print(div_num)


# ex 4

a = int(input("type your first number: "))
b = int(input("type your second number: "))

def squaare():
    for i in range(a, b):
        yield i ** 2

for sqq in squaare():
    print(sqq)


# ex 5

down = int(input("type your down number: "))

def down_f():
    for dw in range(down, 0, -1):
        yield dw ** 2

for d in down_f():
    print(d)

