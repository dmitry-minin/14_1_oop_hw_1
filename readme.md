Feature 1 
В данному проекте реализованы классы Категория и Продукт.
К данным классам написаны тесты, покрывающие их функциональность.
Дополнительно реализована подгрузка данных из файла jsonи и их обработка.
Добавлен run файл для выполнения кода проекта

Feature2 
Класс Category:
- Список товаров сделан приватным.
- Для добавления товаров реализован метод add_product()
- Реализован геттер для вывода списка товаров 
Для класса Product:
- Реализован класс метод new_product, который принимает на вход словарь и возвращает экземпляр класса.
- Атрибут сделан приватным. Реализован геттер и сеттер для получения и установления новой цены. 
- Для сеттера реализована проверка, что новая цена > 0.
- Для сеттера реализована проверка, что новая цена больше прежней. Если цена меньше требуется подтверждение пользователя.
Написаны тесты для новой функциональности.

Feature3
Для класса Product:
- Добавлен метод __str__.
- В классе Category доработан геттер, с учетом этого.
- Реализован метод __add__, который складывает общую стоимость(цена*колличеество) продукта.
Создан новый класс для реализатора итерируемого объекта и итератора CategoryIter.
- Данный класс помогает производить итерацию по товарам одной категории.
Для класса Category:
- Добавлен метод __str__.
Добавлены тесты покрывающие новую функциональность.

Feature 4
От родительского класса Product добавлено 2 дочерних: Smartphone и LawnGrass.
- В данных классах реализован инициализатор и метод super() для отриуетов родительского класса.
- Доработана функциональность сложения. В дочерние классы добавлен метод __add__ и проверка
на то что прибавляется аналогичный продукт, через метод type.
Доработан метод __add__ для родительского класса Product.
- Добавлена проверка, что добавляется объект, который относится к Product и его дочерним класссам.
Добавлены тесты покрывающие новую функциональность