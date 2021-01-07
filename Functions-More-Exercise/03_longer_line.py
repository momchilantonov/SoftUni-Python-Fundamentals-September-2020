from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def longer_line(p1, q1, p2, q2, p3, q3, p4, q4):
    line1 = line_dimension(p1, q1, p2, q2)
    line2 = line_dimension(p3, q3, p4, q4)
    if line1 >= line2:
        result = closest_point(p1, q1, p2, q2)
        print(f"({(result[0])}, {(result[1])})({(result[2])}, {(result[3])})")
    else:
        result = closest_point(p3, q3, p4, q4)
        print(f"({(result[0])}, {(result[1])})({(result[2])}, {(result[3])})")


def line_dimension(p1, q1, p2, q2):
    l_dim = sqrt((p2-p1) ** 2+(q2-q1) ** 2)
    return l_dim


def closest_point(p1, q1, p2, q2):
    point1 = line_dimension(p1, q1, 0, 0)
    point2 = line_dimension(p2, q2, 0, 0)
    if point1 <= point2:
        result = [int(p1), int(q1), int(p2), int(q2)]
        return result
    else:
        result = [int(p2), int(q2), int(p1), int(q1)]
        return result


longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
