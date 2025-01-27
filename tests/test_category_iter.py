from src.category_iter import CategoryIter


def test_category_iteration(category1):
    """
    Тестирование нового класса для создания итерируемого объекта и итератора
    """
    for i in CategoryIter(category1):
        assert i == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
