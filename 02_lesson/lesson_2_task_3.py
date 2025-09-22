import math

def square(side):
    return math.ceil(side ** 2)

square_side = int(input(f" введите длину: "))


print(math.ceil(square(square_side)))