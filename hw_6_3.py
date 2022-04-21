import sys
import json
import csv


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    human_dict = {}
    humans = []
    hobby = []
    with open(path_users_file, 'r', newline='',
              encoding='utf-8') as f_obj:  # Читаем и файл с фио и записываем в список
        reader = csv.reader(f_obj)
        for row in reader:
            humans.append(row)

    with open(path_hobby_file, 'r', newline='',
              encoding='utf-8') as f_obj:  # Читаем и файл с хобби и записываем в список
        reader = csv.reader(f_obj)
        for row in reader:
            hobby.append(row)

    for i in range(len(humans)):  # собираем все в словарь
        human = ",".join(humans[i])
        if i >= len(hobby):
            human_hobby = None
        else:
            human_hobby = ",".join(hobby[i])

        human_dict.update({human: human_hobby})
    return human_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')

with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
