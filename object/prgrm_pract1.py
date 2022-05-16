from platform import java_ver
from re import I


class Vector2d:
    def __init__(self) -> None:
        self.i=i 
        self.j=j
    def printVector(self):
        print(f"{self.i}i+{self.j}j")
class Vector3d(Vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def printVector3d(self):
        print(f)
