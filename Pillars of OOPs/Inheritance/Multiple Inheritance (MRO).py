## Multiple Inheritance (MRO)


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()   # B    
# Why B? Because of MRO (Method Resolution Order) and Why not C? Because B is before C in the class definition of D and Python follows the left-to-right order for method resolution so it checks B first and finds the show method there, hence it executes B's show method and not C's show method as C would be checked only if B did not have the show method.

print(D.__mro__)