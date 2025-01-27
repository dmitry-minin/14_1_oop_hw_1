from src.main import Product
import pytest


def test_product_initialization(product1):
    """
    Тест инициализации продукта
    """
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product_func(new_product_dict):
    """
    Тест функции создания экземпляра Product из словаря
    """
    test_product = Product.new_product(new_product_dict)
    assert isinstance(test_product, Product)
    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


def test_price_getter(product1):
    """
    Тест геттера цены
    """
    assert product1.price == 180000.0


def test_price_setter_higher_price(product1):
    """
    Тест сеттера цены
    """
    product1.price = 200000
    assert product1.price == 200000


def test_price_setter_price_lower_zero(product1):
    """
    Тест сеттера цены равной или меньше нуля, проверка вывода ошибки
    """
    with pytest.raises(ValueError):
        product1.price = -100
    with pytest.raises(ValueError):
        product1.price = 0


def test_price_setter_user_confirm(product1, monkeypatch):
    """
    Тест сеттар цены с подтверждением со стороны пользователя
    """
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product1.price = 150000
    assert product1.price == 150000


def test_price_setter_user_reject(product1, monkeypatch):
    """
    Тест сеттар цены с отказом со стороны пользователя
    """
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product1.price = 130000
    assert product1.price == 180000


def test_product_str(product1):
    """
    Тест конвертации экземпляра Product в строку метод __str__
    """
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product1, product2):
    """
    Тест функциональности сложения атрибутов экземпляров (общая цена) класса методом __add__
    """
    assert product1 + product2 == 2580000.0


def test_add_incorrect_type_to_product(product1):
    """
    Тест попытки сложения экземпляра Product с не-Product объектом
    """
    with pytest.raises(TypeError):
        _ = product1 + 100
    with pytest.raises(TypeError):
        _ = product1 + "string"


def test_product_mixin_print(product1, capsys):
    """
    Тест проверки работы метода миксина PrintInfo
    """
    product1.print_info()
    captured = capsys.readouterr()
    assert captured.out == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)\n"
