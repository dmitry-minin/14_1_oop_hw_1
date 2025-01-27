class MixinProduct:
    """Класс для вывода описания продукта"""

    def __repr__(self) -> str:
        """
        Mixin class Создает строковое описание класса наследника
        """
        name = getattr(self, "name", "Unknown attribute")
        description = getattr(self, "description", "Unknown attribute")
        price = getattr(self, "price", "Unknown attribute")
        quantity = getattr(self, "quantity", "Unknown attribute")
        return f"{self.__class__.__name__}('{name}', '{description}', {price}, {quantity})"

    def print_info(self) -> None:
        """
        Выводит информацию о продукте
        """
        print(repr(self))
