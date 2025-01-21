class Product:
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_dict: dict):
        """
        Класс метод для создания экземпляра Product из словаря
        """

        return cls(name=product_dict.get('name'), description=product_dict.get('description'),
                   price=product_dict.get('price'), quantity=product_dict.get('quantity'))

    @property
    def price(self) -> float:
        """Возвращает текущую цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Устанавливает новую цену товара"""
        if new_price > 0:
            if self.__price > new_price:
                ask_confirmation = input("New price lower than old one. Press y to confirm n to reject saving:  ")
                if ask_confirmation.lower() == 'y':
                    self.__price = new_price
                else:
                    print("Price not saved.")
            else:
                self.__price = new_price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

    def __add__(self, other):
        """Сложение общей цены (price * quantity) двух продуктов"""
        return self.price * self.quantity + other.price * other.quantity


class Category:
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
        total_quantity_of_products = 0
        for product in self.__products:
            total_quantity_of_products += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity_of_products} шт."

    def add_product(self, product: Product):
        """Метод для добавления нового продукта в список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список продуктов в виде текстовой строки"""
        return "\n".join([f"{p}" for p in self.__products])


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    print(category1.products)
    print(category1.products.split("\n"))
