class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name},{self.weight},{self.category}')


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.readlines()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        products_in_file = self.get_products()

        for product in products:
            product_exists = False
            for line in products_in_file:
                product_name_in_file = line.split(',')[0].strip()  
                if product.name == product_name_in_file:
                    product_exists = True
                    break
            if not product_exists:
                file.write(f"{product}\n")
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
