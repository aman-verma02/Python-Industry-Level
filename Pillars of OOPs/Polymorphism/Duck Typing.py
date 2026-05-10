# Duck Typing (VERY PYTHONIC 🔥)
# 💡 Idea
# “If it behaves like a duck, it’s a duck”
# In Python, we don't care about the type of an object, but rather about its behavior. If an object can perform the required operations, it can be used in place of another object, regardless of its actual type. 


class Duck:
    def quack(self):
        return "Quack!" 
    
class Person:
    def quack(self):
        return "I'm not a duck, but I can quack like one!"
    
def make_it_quack(duck):
    print(duck.quack())

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)