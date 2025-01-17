from load_file import data_loader, objects_creator


"""файл для запуска программы """

source_path = "../data/source.json"
data = data_loader(source_path)
categories = objects_creator(data)

number_of_objects = len(categories)
iterator = number_of_objects

print(categories[number_of_objects-1].category_count)
print(categories[number_of_objects-1].product_count)

while iterator > 0:
    print(categories[number_of_objects-iterator].name)
    print(categories[number_of_objects - iterator].description)
    print(categories[number_of_objects - iterator].products)
    iterator -= 1
