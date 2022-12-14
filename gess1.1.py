# put your python code here
from random import *
print('Добро пожаловать в числовую угадайку!!!')
n = randint(1,100)
answer_low = ['Хахаха! Ну ты и фуфел! Я загадал меньшее число. Попробуй ещё разок!', 'Хе-хе. Промашка вышла. Целься ниже...', 'Слишком большое число...', 'Бери ниже...']
answer_high = ['Мимо! Бери большее число!', 'Неть! Слишком маленькое число. Давай большее.', 'Фиаско. Увеличь вводимое число.']
def is_valid():
    if num.isdigit() and 1 <= int(num) and int(num) <= 100:
        return True
    else:
        return False
def start_game():
    while True:
        global num
        global n
        num = input('Введи число от 1 до 100, разрази тебя гром!!' )
        if is_valid() == False:
            print('ТЫ ЧЁ ПЁС ТВОРИШЬ?! От ЕДИНИЦЫ до СТА введи цифру!!')
        if is_valid() == True:
            n = int(n)
            if int(num) < int(n):
                print(choice(answer_high))
            if int(num) > int(n):
                print(choice(answer_low))
            if int(n) == int(num):
                print('Угадал!! Умница, таки попал пальцем в дырку!')
                a = input('Хочешь ещё погадать? Введи "АГА" или "НЕА".' )
                if a == "АГА":
                    n = randint(1,100)
                    continue
                elif a == "НЕА":
                    break
                else:
                    print('Извиняй, чёт совсем не понял твою мысль... Видимо ты переутомился гадая. Иди отдохни.')
                    break
start_game()
print('Заскучаешь, приходи. Погадаем исчЁ!))')