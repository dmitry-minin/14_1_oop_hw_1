from abc import ABC, abstractmethod
from src.mixin_product import MixinProduct


class BaseProduct(ABC):
    """Абстрактный класс для описания продуктов"""
    @abstractmethod
    def __init__(self) -> None:
        """Абстрактный метод для инициализатора"""
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        """Абстрактный метод для сложения двух экземпляров Product"""
        pass


class Product(MixinProduct, BaseProduct):
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity

        super().print_info()

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

    @property
    def quantity(self) -> int:
        """
        Возвращает текущее количество товара
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        """
        Устанавливает новое количество товара, проверяет что оно >= 0
        """
        if new_quantity >= 0:
            self.__quantity = new_quantity
        else:
            raise ValueError("Количество не может быть отрицательным")

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
        """
        Сложение общей цены (price * quantity) двух продуктов Smartphone
        """
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
        """
        Сложение общей цены (price * quantity) двух продуктов Lowngross
        """
        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Вы можете сложить продукт газон только с газоном")
