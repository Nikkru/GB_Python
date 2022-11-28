import model
import view


def button_click():
    # читаем сохранненую базу (json) в словарь
    is_data = model.read_json_in_data('my.json')
    print(is_data)
    # добавляем в словарь нового сотрудника
    is_data.update(model.get_add_new_employee())
    print(is_data)
    # пишем словарь в сохранненую базу (json)
    model.json_file_write(is_data, 'my.json')


def start_menu():
    # читаем сохранненую базу (json) в словарь
    is_data = model.read_json_in_data('my.json')
    print(is_data)
    while True:
        mode = view.get_mode()
        if mode == 1:
            model.get_key(is_data)
        elif mode == 2:
           new_man = model.get_add_new_employee()
           is_data.update(new_man)
           model.json_file_write(is_data, 'my.json')
        elif mode == 3:
            person = input('Введите полное имя сотрудника: ')
            model.get_value(is_data, person, 'phone_number')
        elif mode == 4:
            value_ = input('Введите дожность для списка сотрудников: ')
            model.get_key1_by_value2(is_data,'position', value_)
        elif mode == 5:
            pass
        elif mode == 6:
            pass
        elif mode == 7:
            pass
        elif mode == 8:
            print('Всего хорошего!')
            break
        print('\nДальше?')