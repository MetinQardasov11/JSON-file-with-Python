import json

def add_product(product_name,price,sales_total,categories):
    products = {
        "Product Name" : product_name,
        "Price" : price,
        "Sales Total" : sales_total,
        "Categories" : categories
    }
    
    with open('products.json','w') as file:
        json.dump(products,file,ensure_ascii=False,indent=4)

# add_product('Iphone 13 pro max',1200,True,['phone','electronics'])

def show_product():
    with open('products.json','r') as file:
        data = json.load(file)
    categories = ','.join([category for category in data['Categories']])
    print('Categories: ',categories)
    print(f'Product Name: {data["Product Name"]}\nPrice: {data["Price"]}\nSales Total: {data["Sales Total"]}\nCategories: {data["Categories"]}')

show_product()