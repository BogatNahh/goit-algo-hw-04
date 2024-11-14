def get_cats_info(path):
    cats_info = []  
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Некоректний формат рядка: {line.strip()}")
                    continue
        return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except IOError:
        print("Помилка вводу/виводу при роботі з файлом.")
        return []
