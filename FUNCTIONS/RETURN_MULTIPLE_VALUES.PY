# CREATE A FUCNTION THAT RETURN  BOTH AREA AND CIRCF OF CIRCLE GIVEN IT'S RADIUS.
import math
R=int(input("enter the value of radius:"))
def cirlce_stats(radius):
    area= math.pi*radius**2 # anything after return wil not proceed
    perimeter=2*math.pi*radius
    return(area,perimeter)
area,peri=cirlce_stats(4)
print(f"area is{area:.3f}and perimeter is{peri:.3f}")
    