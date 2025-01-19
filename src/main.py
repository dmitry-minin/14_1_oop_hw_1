class Product:
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    def add_product(self, product: Product):
        """Метод для добавления нового продукта в список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список продуктов в виде текстовой строки"""
        return "\n".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products])


if __name__ == "__main__":
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3]
        )

        print(category1.products)
        product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        category1.add_product(product4)
        print(category1.products)
        print(category1.product_count)

        new_product = Product.new_product(
            {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
             "quantity": 5})
        print(new_product.name)
        print(new_product.description)
        print(new_product.price)
        print(new_product.quantity)

        new_product.price = 20000
        print(new_product.price)

        # new_product.price = -100
        # print(new_product.price)
        # new_product.price = 0
        # print(new_product.price)
