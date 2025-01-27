from abc import ABC, abstractmethod


class BaseCategoryOrder(ABC):
    """
    Абстрактный класс для описания продуктов
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Абстрактный метод для инициализатора
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Абстрактный метод для создания строкового представления продукта
        """
        pass
