import math

a, b, c = map(float, input().split())
d = b*b - (4*a*c)
x1 = (-(b) + math.sqrt(d)) / 2*a
x2 = (-(b) - math.sqrt(d)) / 2*a
print("Первый корень" , {x1} , "Второй корень" , {x2})