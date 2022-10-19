import json

BD={'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
 'phones':  [654644464,6546465646,464566465,86465464465] }  }

def load():
            # загрузить из json
            fname='BD.json' #открываем файл
            with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD_local = json.load(fh)  # загружаем из файла данные в словарь data
            print('БД успещно загружена')
            return BD_local

def save():
            # сохранить в json
            with open('../../Downloads/BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(BD, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            print('БД успещно сохранена')

#save()


BDnew = load ()
print(BDnew)

