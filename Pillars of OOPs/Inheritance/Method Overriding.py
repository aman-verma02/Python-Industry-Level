# ❓ What is it?
# Child modifies parent 


'''


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

b = B()
b.show()   # B


'''




class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()     ## Call the parent method
        print("B")

b = B()
b.show()   # A
           # B