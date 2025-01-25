from src.main import Category
from src.main import Product
from src.main import Smartphone
from src.main import LawnGrass
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


@pytest.fixture
def smartphone_product1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_product2():
    return Smartphone("Iphone 15", "512GB, Gray space",
                      210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_product1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_product2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")


@pytest.fixture(autouse=True)
def reset_class_atributes():
    Category.category_count = 0
    Category.product_count = 0
