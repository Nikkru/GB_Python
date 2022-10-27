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

import random

def who_first():
    if random.randint(0, 1) == 0:
        return True
    else:
        return False

print(who_first())

def man_step(score):
    try:
        i = int(input("your move now: "))
        if 0 < i < 29:
            score -= i
            print(score)
            return score
        else:
            print("Enter correct value!")
    except:
        print("Enter correctly value")

def bot_step(score):
    if not (score - max_step) > 0:
        print("game over! you are loose!")
    elif (score // max_step) % 2 != 0:
        while (score // max_step) % 2 != 0:
            score -= random.randint(1, 29)
            break
        print(score)
    else:
        score -= random.randint(1, 28)
        print(score)
    return score

def bot_vs_man(score, step):
    man_first = who_first()
    man: bool = True
    bot: bool = True
    if man_first == True:
        score = man_step(score)
        man = not man
        bot = not man
    else:
        score = bot_step(score)
    while score > step:
        if man:
            score = man_step(score)
            man = not man
            bot = not man
        else:
            score = bot_step(score)
            bot = not bot
            man = not bot
    else:
        print("game over! You are winner!")

bot_vs_man(2021, 28)