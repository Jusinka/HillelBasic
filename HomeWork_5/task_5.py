import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side

    return (perimeter, area, diagonal)

side_length = 5
result = square(side_length)
print("Периметр:", result[0])
print("Площа:", result[1])
print("Діагональ:", result[2])