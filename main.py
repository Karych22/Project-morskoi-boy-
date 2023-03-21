import math
print('введите координаты точки А')
x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())
z2 = float(input())
d = math.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1)+(z2-z1)*(z2-z1))
print("Ответ задачи")
print(d)
