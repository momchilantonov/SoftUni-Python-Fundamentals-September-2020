p1 = float(input())
q1 = float(input())
p2 = float(input())
q2 = float(input())


def p_closest(x1, y1, x2, y2):
    dis_1 = x1 ** 2+y1 ** 2
    dis_2 = x2 ** 2+y2 ** 2
    if dis_1 <= dis_2:
        k = (int(x1), int(y1))
        return k
    else:
        k = (int(x2), int(y2))
        return k


print(p_closest(p1, q1, p2, q2))
