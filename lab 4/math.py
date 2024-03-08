
import math

# degree to radian
degree = int(input("your degree: "))

print(math.radians(degree))


# area of trapezoid

height = int(input("your height: "))
base_1 = int(input("your base 1: "))
base_2 = int(input("your base 2: "))

print( (base_1+base_2)*height/2)


# area of regular polygon

side = int(input("your side: "))
length = int(input("your length: "))

angle = 180/side
tan_value = 1/2 * math.tan(angle)
print(tan_value)

print( (side * length * tan_value) /2 )


# area of parra

base_par = float(input("your base par: "))
height_par = float(input("your par height: "))

print(base_par * height_par)