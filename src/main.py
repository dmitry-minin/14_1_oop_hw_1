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
        """
        Устанавливает новую цену товара при условии, что она больше 0.
        Если цена ниже текущей - необходимо подтверждение пользователя
        """
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
        """
        Сложение общей цены (price * quantity) двух продуктов,
        при условии, что они являются экземплярами одного класса
        """
        if isinstance(other, self.__class__):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Вы можете сложить продукты только с продуктами")


class Smartphone(Product):
    """
    Класс для описания продукта - смартфона
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение общей цены (price * quantity) двух продуктов Smartphone"""
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Вы можете сложить смартфоны только со смартфонами")


class LawnGrass(Product):
    """
    Класс для описания продукта - газонной травы
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение общей цены (price * quantity) двух продуктов Lowngross"""
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Вы можете сложить продукт газон только с газоном")


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


if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
