# write code to represent 2D vector class and use it to create another 3D vector class

class Vector2D:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")
    
class Vector3D(Vector2D):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
    
v2d = Vector2D(3, 4)
v3d = Vector3D(5, 6, 7)
v2d.show()
v3d.show()