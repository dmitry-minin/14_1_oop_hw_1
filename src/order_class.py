from src.product_class import Product
from src.category_order_base_class import BaseCategoryOrder


class Order(BaseCategoryOrder):
    """
    Класс для описания заказа
    """
    def __init__(self, product: Product, order_quantity: int = 0):
        self.product = product
        if order_quantity < 0:
            raise ValueError("Количество заказанного продукта не может быть отрицательным")
        elif order_quantity > product.quantity:
            raise ValueError(f"Недостаточное количество товара на складе, остаток {product.quantity}")
        self.order_quantity = order_quantity
        self.total_price = self.product.price * self.order_quantity

        self.update_product_quantity()

    def __str__(self):
        """
        Создает строковое описание заказа
        """
        return f"{self.__class__.__name__}({self.product}, {self.order_quantity})"

    def update_product_quantity(self):
        """
        Обновляет остаток товара на после заказа
        """
        new_quantity = self.product.quantity - self.order_quantity
        self.product.quantity = new_quantity
