def calculate_area(value1, value2, shape_type="triangle"):
    if shape_type == "triangle":
        area = 0.5 * value1 * value2
    elif shape_type == "square":
        area = value1 * value2
    else:
        raise ValueError("Непідтримуваний тип фігури")

    return area

area_triangle = calculate_area(5, 8)
print("Площа трикутника:", area_triangle)


area_square = calculate_area(4, 4, shape_type="square")
print("Площа квадрата:", area_square)