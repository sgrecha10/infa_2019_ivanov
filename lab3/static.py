
class Cylinder:
    @staticmethod
    def make_area(d, h):
        return (d + h)*2

    def __init__(self, diametr, height):
        self.dia = diametr
        self.h = height
        self.__area = Cylinder.make_area(self.dia, self.h)

    def getArea(self):
        return self.__area

    def __setattr__(self, key, value):
        if key == "h":
            self.__dict__[key] = value
            if hasattr(self, "dia"):
                self.__dict__['_Cylinder__area'] = Cylinder.make_area(self.dia, self.h)
        if key == "dia":
            self.__dict__[key] = value
            if hasattr(self, "h"):
                self.__dict__['_Cylinder__area'] = Cylinder.make_area(self.dia, self.h)
        if key == "_Cylinder__area":
            self.__dict__[key] = value


a = Cylinder(50, 10)
# print(a.dia, a.h, a._area)
print(a.dia, a.h, a.getArea())
a.dia = 1
a.h = 5
print(a.dia, a.h, a.getArea())
a._Cylinder__area = 33
print(a.dia, a.h, a.getArea())