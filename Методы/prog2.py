class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x), str(self.y), str(self.z)

    def __add__(self, newV):
        return (self.x + newV.x), (self.y + newV.y), (self.z + newV.z)

    def __sub__(self, newV):
        return (self.x - newV.x), (self.y - newV.y), (self.z - newV.z)

    def __mul__(self, newV):
        return (self.x * newV.x), (self.y * newV.y), (self.z * newV.z)
