from src.main import Category
from src.main import Product


class CategoryIter:
    """Класс для итерирования по категориям"""

    def __init__(self, category: Category):
        self.category = category
        self.products = self.category.products.split("\n")

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start >= len(self.products):
            raise StopIteration
        product_in_list = self.products[self.start]
        self.start += 1
        return product_in_list


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3])

    for product in CategoryIter(category1):
        print(product)
