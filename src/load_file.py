import json
import os
from src.main import Category, Product


def data_loader(path: str) -> list:
    """функция, которая получает данные из json файла и преобразует их в список"""
    file_path = os.path.abspath(path)
    with open(file_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def objects_creator(data_source: list[dict]) -> list:
    """функция, которая преобразует список словарей в список экземпляров классов"""
    categories = []
    for c in data_source:
        products = [Product(p["name"], p["description"], p["price"], p["quantity"]) for p in c["products"]]
        categories.append(Category(c["name"], c["description"], products))
    return categories
