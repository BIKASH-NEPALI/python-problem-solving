class Point:
    def __init__(self,x, y):
        self.x_cordinate=x
        self.y_cordinate=y
    def __str__(self):
        return (f"{self.x_cordinate},{self.y_cordinate}")
    def distance_betwen_points(self,other):
        return (((self.x_cordinate-other.x_cordinate)**2+(self.y_cordinate-other.y_cordinate)**2)**0.5)
    def distance_from_origin(self):
        return (((self.x_cordinate)**2+(self.y_cordinate)**2)**0.5)
        
P1=Point(-1,-1)
print(P1)
P2=Point(-3,5)
print(P2)
print(P1.distance_betwen_points(P2))
print(P1.distance_from_origin())
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return (f"{self.A}x+{self.B}y+{self.C}=0")
    def point_on_line(self,P):
        if self.A*P.x_cordinate+self.B*P.y_cordinate+self.C==0:
            print("lie on the line")
        else:
            print("does not lie on the line")
    def distance_line_points(self,P):
        den=((self.A**2+self.B**2)**0.5)
        nume=(self.A*P.x_cordinate+self.B*P.y_cordinate+self.C)
        return (nume/den)
L1=Line(1,2,3)
print(L1)
L1.point_on_line(P1)
print(L1.distance_line_points(P1))