class cir:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

r = float(input("enterr the radius: "))
c = cir(r)

print("area is ", c.area())
print("perimeter iss", c.perimeter())