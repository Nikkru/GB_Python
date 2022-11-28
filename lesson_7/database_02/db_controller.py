import db_model as model
import db_view as view

employees = model.read_csv()
# db_base = model.json_file_read('database.json')
db_base = {}


def start_menu():
    while True:
        mode = view.get_mode()
        if mode == 1:
            search_key = model.get_key(view.get_search_key())
            search_empl = view.get_search_empl("данные для поиска")
            found_empl = model.find_employee(employees, search_key, search_empl)
            view.print_to_console_found_empl(found_empl)
        elif mode == 2:
            name_pos = view.get_search_by_position()
            list_empl_pos = model.get_list_empl_by_pos(employees, name_pos)
            view.print_to_console_celection(list_empl_pos)
        elif mode == 3:
            hi, lo = view.get_salary_range()
            list_empl_salary = model.find_employees_by_salary_range(employees, float(hi), float(lo))
            view.print_to_console_celection(list_empl_salary)
        elif mode == 4:
            data_new_empl = view.get_add_new_employee()
            model.append_to_csv(model.get_last_id(), data_new_empl)
            db_base.update(data_new_empl)
            model.json_file_write(db_base, 'database.json')
        elif mode == 5:
            last_name_empl = view.get_search_empl("фамилию")
            employees_without = model.del_employee(employees, last_name_empl)
            model.write_csv(employees_without)
        elif mode == 6:
            last_name_empl = view.get_search_empl("обновить данные какого")
            new_data = view.get_add_new_employee()
            employees_rep = model.replacement_employee(employees, last_name_empl, new_data)
            model.write_csv(employees_rep)
            model.write_json(db_base)
            model.json_file_write(db_base, 'database.json')
        elif mode == 7:
            model.export_data_json(employees)
        elif mode == 8:
            model.write_csv(employees)
        elif mode == 9:
            print('Всего хорошего!')
            break
        print('\nДальше?')