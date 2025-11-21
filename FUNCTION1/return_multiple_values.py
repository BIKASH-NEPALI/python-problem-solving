import math
radius=int(input("Enter the radius"))
def circleStat(radius):
    area= math.pi*radius**2
    circ=2*math.pi*radius
    return area, circ
a,c=circleStat(radius)
print(a,c)
