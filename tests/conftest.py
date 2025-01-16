from src.main import Category
from src.main import Product
import pytest


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)



@pytest.fixture
def category1(product1):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                 " но и получения дополнительных функций для удобства жизни", [product1])
