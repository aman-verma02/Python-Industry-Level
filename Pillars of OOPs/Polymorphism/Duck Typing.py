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





# What is duck typing? 
# Duck typing is a programming concept in which the type or class of an object is less important than the methods it defines or the behavior it exhibits. In duck typing, if an object can perform the required operations (i.e., it has the necessary methods), it can be used in place of another object, regardless of its actual type. The name "duck typing" comes from the phrase "If it looks like a duck and quacks like a duck, then it is a duck." This approach allows for more flexible and dynamic code, as it focuses on what an object can do rather than what it is.
# “Objects are used based on behavior, not type.”