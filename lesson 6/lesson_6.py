import random

field = []

for i in range(3):
    field_row = []
    for j in range(3):
        field_row.append('_')
    field.append(field_row)


def print_field(f):
    for i in range(3):
        print('   '.join(f[i]))


def check_win(field_list):
    for row in range(3):
        if field_list[row][0] == field_list[row][1] == field_list[row][2] != "_": return True
    for column in range(3):
        if field_list[0][column] == field_list[1][column] == field_list[2][column] != "_": return True
    if field_list[0][0] == field_list[1][1] == field_list[2][2] != "_": return True
    if field_list[2][0] == field_list[1][1] == field_list[0][2] != "_": return True


def player_move(field_print):
    move = input("Введите координаты вашего хода через запятую: ")
    move_coordinate = move.split((','))
    x = int(move_coordinate[0])
    y = int(move_coordinate[1])
    field[x][y] = 'x'

    return field_print


def comp_move(field_print):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while field[x][y] != '_':
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    field[x][y] = 'o'
    return field_print


print_field(field)

for m in range(9):
    if m % 2 == 0:
        field = player_move(field)
        if check_win(field):
            print('You are winner')
            break
    else:
        field = comp_move(field)
        if check_win(field):
            print('You are looser')
            break
    print_field(field)


