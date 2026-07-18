# Q. Product Store
#     * Design & create an online store for products (name, price).
#     * Track total products being created
#     * Create a static method to calculate discount on each product based on a % parameter.

class Product:
    count = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
        
    def get_info(self):  #instance method
        print(f"price of {self.name} is Rs.{self.price}")
        
    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")
    
    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount/ 100)}")
        
p1 = Product("phone", 10_000)
p2 = Product("Tablet", 30_000)
p3 = Product("laptop", 50_000)

p1.get_info()
Product.get_count()
p1.calc_discount(10_000, 12)
p1.calc_discount(p1.price, 12)