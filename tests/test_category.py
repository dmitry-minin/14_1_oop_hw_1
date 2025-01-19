def test_category_initialization(category1):
    """Тест инициализации категории с продуктом"""
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации,"
                                     " но и получения дополнительных функций для удобства жизни")
    assert category1.products == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert category1.category_count == 1
    assert category1.product_count == 1


def test_add_product(category1, product1):
    """Тест функции добавления нового продукта в категории, заодно проверяем работу геттера products"""
    assert category1.product_count == 1
    category1.add_product(product1)
    assert category1.product_count == 2
    assert category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.')
