# задача 1. Создайте программу для игры с конфетами человек против бота.
# Условие задачи:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""
#
# import random
#
# def who_first():
#     if random.randint(0, 1) == 0:
#         return True
#     else:
#         return False
#
# print(who_first())
#
# def man_step(score):
#     try:
#         i = int(input("your move now: "))
#         if 0 < i < 29:
#             score -= i
#             print(score)
#             return score
#         else:
#             print("Enter correct value!")
#     except:
#         print("Enter correctly value")
#
# def bot_step(score):
#     if not (score - max_step) > 0:
#         print("game over! you are loose!")
#     elif (score // max_step) % 2 != 0:
#         while (score // max_step) % 2 != 0:
#             score -= random.randint(1, 29)
#             break
#         print(score)
#     else:
#         score -= random.randint(1, 28)
#         print(score)
#     return score
#
# def bot_vs_man(score, step):
#     man_first = who_first()
#     man: bool = True
#     bot: bool = True
#     if man_first == True:
#         score = man_step(score)
#         man = not man
#         bot = not man
#     else:
#         score = bot_step(score)
#     while score > step:
#         if man:
#             score = man_step(score)
#             man = not man
#             bot = not man
#         else:
#             score = bot_step(score)
#             bot = not bot
#             man = not bot
#     else:
#         print("game over! You are winner!")
#
# bot_vs_man(2021, 28)

# задача 2.
# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.

reading_file = "hw5task2.txt"
writing_file = "hw5task2_write.txt"
def write_file(W,R):
    with open(W, 'w') as data:
        data.write(R)
def read_file(N):
    with open(N, 'r') as N:
        for line in N:
            return line

def rle_encode(string_a):
    str_encode = ''
    count = 1
    char = string_a[0]
    for i in range(1, len(string_a)):
        if string_a[i] == char:
            count += 1
        else:
            str_encode += str(count)+char
            char = string_a[i]
            count = 1
            str_encode += str(count)+char
    # print(str_encode)
    return str_encode

def rle_decode(str_encode):
    decode_str = ''
    char_len =''
    for i in range(len(str_encode)):
        if decode_str[i].isdigit():
            char_len += str_encode[i]
        else:
            decode_str += str_encode[i] * int(char_len)
        char_len = ''
    # print(decode_str)
    return decode_str

string_for_encode = read_file(reading_file)
string_encoded = rle_encode(string_for_encode)
write_file(writing_file, string_encoded)

print(f'text for encode - {string_for_encode}')
print(f'text encoded - {string_encoded}')