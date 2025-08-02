# def multiply(x, y):
def multiply(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


print(multiply(2, 3))
