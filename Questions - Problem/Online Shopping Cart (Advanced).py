'''
❓ Problem
Add:
item + price + quantity
remove item
apply discount
total price

🧠 Thinking
Use:
dictionary → item → (price, quantity)

'''

class Cart:
    def __init__(self):
        self.items = {}  # item → [price, quantity]

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item][1] += quantity
        else:
            self.items[item] = [price, quantity]

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        total = 0
        for price, qty in self.items.values():
            total += price * qty
        return total

    def apply_discount(self, percent):
        return self.total_price() * (1 - percent / 100)



cart = Cart()
cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 1000, 2)

print(cart.total_price())
print(cart.apply_discount(10))