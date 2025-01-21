from src.main import Category
from src.main import Product
import pytest


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category1(product1):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                 " но и получения дополнительных функций для удобства жизни", [product1])


@pytest.fixture
def new_product_dict():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0, "quantity": 5}


@pytest.fixture(autouse=True)
def reset_class_atributes():
    Category.category_count = 0
    Category.product_count = 0
