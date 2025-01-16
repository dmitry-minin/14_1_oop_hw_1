def test_category_initialization(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации,"
                                     " но и получения дополнительных функций для удобства жизни")
    assert len(category1.products) == 1
    assert category1.category_count == 1
    assert category1.product_count == 1
