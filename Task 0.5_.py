import math


def area_of_triangle(side1, side2, side3):
    """
    s=semiperimeter of a triangle

    """
    s = (side1 + side2 + side3) * 0.5
    return math.sqrt(s * ((s - side1) * (s - side2) * (s - side3)))  # formula of a triangle using semiperimeter


area_of_triangle()
