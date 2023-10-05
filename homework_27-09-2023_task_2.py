'''
Задача № 2:
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
'''

import os
import json
import csv
import pickle

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

crawl_directory("C:\GeekBrains_Immersion_in_Python","C:\GeekBrains_Immersion_in_Python\Lesson_16_Seminar_8_27-09-2023_19-00")
