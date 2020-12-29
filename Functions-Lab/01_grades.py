def grades(grade):
    result = None
    if 2 <= grade <= 2.99:
        result = 'Fail'
    elif 3 <= grade <= 3.49:
        result = 'Poor'
    elif 3.5 <= grade <= 4.49:
        result = 'Good'
    elif 4.5 <= grade <= 5.49:
        result = 'Very Good'
    elif 5.5 <= grade <= 6.00:
        result = 'Excellent'
    return result


grade_point = float(input())

print(grades(grade_point))
