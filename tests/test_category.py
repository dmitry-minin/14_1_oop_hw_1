import pytest
from src.category_class import Category


def test_category_init(category1):
    """
    Тест инициализации категории с продуктом
    """
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации,"
                                     " но и получения дополнительных функций для удобства жизни")
    assert category1.products == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert category1.category_count == 1
    assert category1.product_count == 1


def test_add_product(category1, product1):
    """
    Тест функции добавления нового продукта в категории, заодно проверяем работу геттера products
    """
    assert category1.product_count == 1
    category1.add_product(product1)
    assert category1.product_count == 2
    assert category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.')


def test_add_product_other_type(category1):
    with pytest.raises(TypeError):
        _ = category1.add_product(123)
    with pytest.raises(TypeError):
        _ = category1.add_product(["New bicycle", 200000])


def test_category_str(category1):
    """
    Тест конвертации экземпляра Category в строку метод __str__
    """
    assert str(category1) == 'Смартфоны, количество продуктов: 5 шт.'


def test_category_middle_price(category1):
    """
    Тест метода products_avg_price подсчитывающего среднюю цену
    """
    assert category1.middle_price() == 180000.0


def test_category_middle_price_exception():
    """
    Тестирование исключения когда список пустой, должен вернуться ноль
    """
    test_category = Category("Empty category", "Empty description", [])
    assert test_category.middle_price() == 0
