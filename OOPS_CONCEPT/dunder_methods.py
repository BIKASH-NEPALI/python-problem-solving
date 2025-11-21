class Fraction:
    def __init__(self, x, y):# parameterized constructor
        self.num=x
        self.den=y
    def __str__(self):
        return (f"{self.num}/{self.den}")
    def __add__(self, other):
        new_num=self.num*other.den + self.den*other.num
        new_den=self.den*other.den
        return (f"{new_num/new_den}")
        
obj=Fraction(3,9)
obj1=Fraction(8,7)
print(obj+obj1)
print(obj)