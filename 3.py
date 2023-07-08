class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        self.products.append({'product': product, 'quantity': quantity})

    def get_products(self):
        if len(self.products) == 0:
            return 'Empty'
        products = ''
        for p in self.products:
            product = p['product']
            quantity = p['quantity']
            products += f"{p['product'].name} x {quantity} = {quantity * product.price}\n"
        return products.rstrip('\n')
    
    def get_cost(self):
        total = 0
        for p in self.products:
            total += p['product'].price * p['quantity'] 
        return total

    def remove_product(self, product):
        for p in self.products:
            if product.name == p['product'].name:
                self.products.remove(p)
    
    def clear_cart(self):
        self.products = []


sugar = Product('Sugar', 50)
apple = Product('Apple', 30)
bread = Product('Bread', 30)

cart = Cart()

cart.add_product(sugar, 2)
cart.add_product(apple, 1)
cart.add_product(bread, 3)

print(cart.get_products())
print(cart.get_cost())
cart.remove_product(apple)
print(cart.get_products())
cart.clear_cart()
print(cart.get_products())

    