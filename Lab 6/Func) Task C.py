import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Считываем четыре действительных числа
x1, y1, x2, y2 = map(float, input().split())

# Вычисляем расстояние и выводим результат
result = distance(x1, y1, x2, y2)
print("{:.5f}".format(result))
