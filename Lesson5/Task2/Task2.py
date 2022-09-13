
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

# Основной метод. реализует 2 варианта игры (человек с человеком и человек с компьютером)
# count - начальное число конфет
# maxitems - максимальное число конфет которое можно взять за ход
# computer - усле True то игра человек с компьютером
def game(count: int, maxitems: int, computer: bool):
    Names = NamesInput(computer)

    gamer = random.randint(0, 10) % 2  # случайно выбираем кто ходит первым

    n = 0
    while True:
        if gamer and computer:
            n = computer_input(count, maxitems)
        else:
            n = player_input(count, maxitems, Names[gamer])
        count -= n
        if count == 0:
            print(f"\nИгрок {Names[gamer]} выиграл!")
            return

        gamer = (gamer + 1) % 2  # Ход следующего игрока


# Присваиваем имена игроков
def NamesInput(computer: bool):
    if computer:
        return [input("Введите имя игрока: "), "компьютер"]
    else:
        return [input("Введите имя 1 игрока: "), input("Введите имя 2 игрока: ")]

#ввод хода игрока человека
def player_input(count: int, maxitems: int, name: str):
    while True:
        _max = min(maxitems, count)
        n = int(input(
            f"Ход игрока {name}. Всего конфет: {count}. Введите число конфет [1..{_max}]: "))
        if n > 0 and n <= _max:
            return n
        print("Ошибка! Попробуйте снова...")

#ход компьютера
def computer_input(count: int, maxitems: int):
    n = count % (maxitems + 1)
    if n == 0:
        n = 1  # Невыгодный расклад... ждем ошибки человека..
    print(f"Ход компьютера. Всего конфет: {count}. Беру: {n}")
    return n


game(2021, 28, False)  # Игра с человеком
game(2021, 28, True)  # Игра с компьютером
