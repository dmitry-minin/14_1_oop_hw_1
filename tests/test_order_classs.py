from src.order_class import Order
import pytest


def test_order_init_successful(order1):
    """
    Тестирование init для класса ордер и сеттера для продукта с обновленным количеством товара
    :param order1:
    :return:
    """
    assert order1.product.name == "Samsung Galaxy S23 Ultra"
    assert order1.product.description == "256GB, Серый цвет, 200MP камера"
    assert order1.product.price == 180000.0
    assert order1.product.quantity == 2
    assert order1.order_quantity == 3
    assert order1.total_price == 540000.0


def test_order_init_value_error(order1):
    """
    Тестирование init для класса ордер с некорректным значением order_quantity
    """
    with pytest.raises(ValueError):
        Order(order1.product, 6)


def test_order_str(order1):
    """
    Тестирование метода str для заказа
    """
    assert str(order1) == "Order(Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт., 3)"
