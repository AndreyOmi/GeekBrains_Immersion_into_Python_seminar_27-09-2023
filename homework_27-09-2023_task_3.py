'''
Задача № 3:
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.
'''

import os
import json
import csv
import pickle

'''
Задача из домашнего задания № 2:
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
'''
def crawl_directory(directory_path, output_path):
    # Список для хранения результатов обхода директории
    crawl_results = []

    def get_directory_size(dir_path):
        # Расчет размера директории и её содержимого
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size

    # Рекурсивный обход директории и поддиректорий 
    for root, dirs, files in os.walk(directory_path):
        dir_size = get_directory_size(root)
        crawl_results.append({
            "Родительская директория": os.path.relpath(root, directory_path),
            "Имя": os.path.basename(root),
            "Тип": "папка",
            "Размер в байтах": dir_size
        })

        for file_name in files:
            file_path = os.path.join(root, file_name)
            crawl_results.append({
                "Родительская директория": os.path.relpath(root, directory_path),
                "Имя": file_name,
                "Тип": "файл",
                "Размер в байтах": os.path.getsize(file_path)
            })

    # Сохранение результатов обхода директории в JSON файл
    with open(os.path.join(output_path, "results.json"), "w") as json_file:
        json.dump(crawl_results, json_file, indent=4)

    # Сохранение результатов обхода директории в CSV файл
    with open(os.path.join(output_path, "results.csv"), "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Родительская директория", "Имя", "Тип", "Размер в байтах"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(crawl_results)

    # Сохранение результатов обхода директории в Pickle файл
    with open(os.path.join(output_path, "results.pkl"), "wb") as pickle_file:
        pickle.dump(crawl_results, pickle_file)

# Проверка разработанной функции:
# Замените первый аргумент этой функции на полный путь к директории, которую Вы хотите сканировать
# Замените второй аргумент этой функции на полный путь к директории, в которую Вы хотите сохранить результаты (созданные файлы)

'''
Задача семинара № 1:
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали 
текстовый файл с псевдо именами и произведением чисел.
📌 Напишите функцию, которая создаёт из созданного ранее 
файла новый с данными в формате JSON. 
📌 Имена пишите с большой буквы. 
📌 Каждую пару сохраняйте с новой строки.
'''

def convert_to_json(input_file, output_file):
    data = []

    with open(input_file, 'r') as file:
        for line in file:
            # Разделение строки на строковую переменную и число через '|'
            parts = line.strip().split('|')
            if len(parts) == 2:
                string_value = parts[0].strip().capitalize()
                number_value = float(parts[1].strip())
                data.append({"String": string_value, "Number": number_value})

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

'''
Задача семинара №2:
📌 Напишите функцию, которая в бесконечном цикле 
запрашивает имя, личный идентификатор и уровень 
доступа (от 1 до 7). 
📌 После каждого ввода добавляйте новую информацию в 
JSON файл. 
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключём для имени. 
📌 Убедитесь, что все идентификаторы уникальны независимо 
от уровня доступа. 
📌 При перезапуске функции уже записанные в файл данные 
должны сохраняться.

'''

def manage_users():
    try:
        with open("users.json", "r") as file: # файл создается вновь, если он не существует
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    while True:
        name = input("Введите имя пользователя (для выхода введите слово exit): ").strip()
        if name.lower() == 'exit':
            break
        
        user_id = input("Введите идентификатор пользователя (для выхода введите слово exit): ").strip()
        if user_id.lower() == 'exit':
            break
        
        access_level = input("Введите уровень доступа (число от 1 до 7): ").strip()
        if access_level.lower() == 'exit':
            break
        
        if not access_level.isdigit() or not 1 <= int(access_level) <= 7:
            print("Вы не правильно ввели уровень. Значение должно быть числом от 1 до 7 (включительно).")
            continue
        
        access_level = int(access_level)
        
        users[user_id] = {"Имя": name, "Уровень_доступа": access_level}
        
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        
        print(f"Пользователь '{name}' с индификатором '{user_id}' и уровнем доступа '{access_level}' добавлен в файл users.json.")

if __name__ == "__main__":
    # Проверка функции задачи № 2 из домашнего задания:
    # Замените первый аргумент этой функции на полный путь к директории, которую Вы хотите сканировать
    # Замените второй аргумент этой функции на полный путь к директории, в которую Вы хотите сохранить результаты (созданные файлы)
    crawl_directory("C:\GeekBrains_Immersion_in_Python","C:\GeekBrains_Immersion_in_Python\Lesson_16_Seminar_8_27-09-2023_19-00")
    
    # Проверка функции задачи № 1 семинара:
    input_file = 'file_seminar_task_3.txt'
    output_file = 'file_seminar_task_3.json'
    convert_to_json(input_file, output_file)
    
    # Проверка функции задачи № 2 семинара:
    manage_users()

