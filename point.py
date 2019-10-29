
class Point:
    '''Point class that plots 3 points'''

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x:{self.x}, y:{self.y}, z:{self.z})"

    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y and self.z == other.z
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)


if __name__ == '__main__':
    p = Point(3,5,7)
    print(p)
    p1 = Point(5,6,8)
    print(p1)
    p3 = p1 + p
    print(p3)