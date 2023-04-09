from collections import Counter
from urllib import request


def symbol_counter_from_url(url: str = 'https://python.org', target_file: str = 'readme.md') -> None:
    """
    В этой функции мы получаем содержимое python.org с помощью встроенной библиотеки urllib, преобразуем прочитанные
    байты в строку и отдаём получившуюся строку в класс Counter из библиотеки collections, который выдаёт словарь с
    количеством вхождений каждого символа в строку. После этого открываем файл readme.md и записываем туда получившийся
    Counter предварительно переведя его в строку
    """
    response = request.urlopen(url)
    count = Counter(str(response.read()))
    with open(target_file, 'w') as f:
        f.write(str(count))
