class QuantityException(ValueError):
    """
    Общий класс для обработки количественных ошибок
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная количественная ошибка"

    def __str__(self):
        """
        Возвращает сообщение об ошибке
        """
        return self.message


class OrderQuantity(QuantityException):
    """
    Класс для обработки ошибок заказа с нулевым или отрицательным количеством товара
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ("Количество товара в заказе не может быть нулевым "
                                             "или отрицательным")


class OrderLowQuantity(OrderQuantity):
    """
    Класс для обработки ошибок с заказом превышающим остаток на складе
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Недостаточное количество товара на складе"
