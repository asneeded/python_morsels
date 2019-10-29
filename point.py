
class Point:
    '''Point class that plots 3 points'''

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x:{self.x}, y:{self.y}, z:{self.z})"
    


if __name__ == '__main__':
    p = Point(3,5,7)
    print(p)