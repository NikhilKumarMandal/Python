import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circ = 2 * math.pi * radius
    return area, circ


a,c = circle_stats(3)

print("Area : ",round(a,2 ),",","Circumference",round(c,2))