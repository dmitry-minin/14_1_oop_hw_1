import pytest


def test_lawngrass_init(lawn_grass_product1):
    """
    Тест конструктора LawnGrass
    """
    assert lawn_grass_product1.name == "Газонная трава"
    assert lawn_grass_product1.description == "Элитная трава для газона"
    assert lawn_grass_product1.price == 500.0
    assert lawn_grass_product1.quantity == 20
    assert lawn_grass_product1.country == "Россия"
    assert lawn_grass_product1.germination_period == "7 дней"
    assert lawn_grass_product1.color == "Зеленый"


def test_lawngrass_add(lawn_grass_product1, lawn_grass_product2):
    result = lawn_grass_product1 + lawn_grass_product2
    assert result == 16750


def test_lawngrass_add_incorrect_product(lawn_grass_product1, smartphone_product1):
    with pytest.raises(TypeError):
        _ = lawn_grass_product1 + smartphone_product1
