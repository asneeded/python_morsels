
import math

class Circle:
    def __init__(self, radius=1):
        if radius < 0 :
            raise ValueError("Radius cant be negative")
        self.radius = radius
    


    
    def __repr__(self):
        return f"Circle({int(self._radius)})"

    @property 
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("Radious cannot be negative")
        self.diameter = val * 2

    @property
    def diameter(self):
        return self._radius * 2
    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return math.pi * (self._radius **2)
    @area.setter
    def area(self, val):
        raise AttributeError()

if __name__ == '__main__':
    c = Circle(2)
    print(c)
    print(c.area)
    print(math.pi * (c.radius ** 2))
