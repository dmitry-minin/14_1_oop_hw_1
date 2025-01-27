from src.product_class import Product
from src.category_order_base_class import BaseCategoryOrder


class Category(BaseCategoryOrder):
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        """
        Строковое представление категории
        """
        total_quantity_of_products = 0
        for product in self.__products:
            total_quantity_of_products += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity_of_products} шт."

    def add_product(self, product: Product):
        """
        Метод для добавления нового продукта в список.
        Проверяет, что добавляемый продукт является экземпляром Product.
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавляемый продукт не относится к продуктам")

    @property
    def products(self) -> str:
        """
        Возвращает список продуктов в виде текстовой строки
        """
        return "\n".join([f"{p}" for p in self.__products])
