from pathlib import Path
from pprint import pprint # Підключаємо для гарного виводу

def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        cat_id, name, age = line.split(',')
                        cats.append({"id": cat_id, "name": name, "age": age})
                    except ValueError:
                        print(f"Неправильний формат рядка або значення віку: {line}")
    except:
        print(f"Файл за шляхом {path} не знайдено.")
    pprint(cats,sort_dicts=False) # Відміняємо сортування та забираємо друк до функції у випадку ще одного друку чомусь отримуємо None



cats_info = get_cats_info("cats_file.txt")
# print(cats_info) # Цей друк не спрацьовуе, отримуємо None