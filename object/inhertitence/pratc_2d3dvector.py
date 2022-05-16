from platform import java_ver


class vector2d:
    def __init__(self,i,j) -> None:
        self.i=i
        self.j=j
    def vector(self):
        print(f"{self.i}i+{self.j}j")

class vector3d(vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def vector(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")
v1=vector2d(1,2)
v2=vector3d(1,2,3)

v1.vector()
v2.vector()

