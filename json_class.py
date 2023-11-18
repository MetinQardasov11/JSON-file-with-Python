import json

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

product_1 = Product('iphone 12',850)
product_2 = Product('iphone 13 pro',950)

products = [product_1.__dict__, product_2.__dict__]
print(products)

with open('class-product.json','w') as file:
    json.dump(products,file,ensure_ascii=False,indent=4)
    
    
with open('class-product.json') as file:
    data = json.load(file)

products_list = []
for p in data:
    products_list.append(Product(p['name'],p['price']))

print(products_list)