import csv
import json
import os


def addTask(file, id):
    """Открытие csv, преобразование в словарь, запись в json файл, удаление csv"""
    with open(file) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
        dr = {}
        for i in reader:
            dr[i[0]] = {"question": i[1], 'variants': i[2].split('/'), "answer": i[3]}
    data = None
    with open('db/tasks.json', "r") as cat_file:
        if os.path.getsize("db/tasks.json") > 0:
            data = json.load(cat_file)
    with open('db/tasks.json', "w") as cat_file:
        if data:  # Если есть другие тесты
            data[id] = dr
            cat_file.write(json.dumps(data, ensure_ascii=False))
        else:
            cat_file.write(json.dumps({id: dr}, ensure_ascii=False))
    os.remove(file)


def editTask(file, id):
    """Открытие csv, преобразование в словарь, пеоезапись json файла, удаление csv"""
    with open(file) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
        dr = {}
        for i in reader:
            dr[i[0]] = {"question": i[1], 'variants': i[2].split('/'), "answer": i[3]}

    with open('db/tasks.json', "r") as cat_file:
        data = json.load(cat_file)
        data[str(id)] = dr
    with open('db/tasks.json', "w") as cat_file:
        cat_file.write(json.dumps(data, ensure_ascii=False))
    os.remove(file)


def deleteTask(id):
    """Удаление теста по id и перезапись json файла"""
    with open('db/tasks.json', "r") as cat_file:
        data = json.load(cat_file)
        data.pop(str(id), None)
    with open('db/tasks.json', "w") as cat_file:
        cat_file.write(json.dumps(data, ensure_ascii=False))
