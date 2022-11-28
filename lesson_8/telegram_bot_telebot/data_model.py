import json

data_ = []

def save(json_file):
    with open(json_file, 'w', encoding="utf-8") as file:
        file.write(json.dumps(data_, ensure_ascii=False))
    print(f'Новая программа сохранена в файле : {json_file}')


def load(json_file):
    global data_
    with open(json_file, 'r', encoding="utf-8") as file:
        data_ = json.load(file)
    print(f'Афиша {json_file} загружена в список "data_"')