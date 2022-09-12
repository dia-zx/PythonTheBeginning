# Создайте программу для игры в ""Крестики-нолики"".

import random


#
def Game(computer : bool):
    Names = NamesInput(computer) 
    board = [[0 for x in range(0, 3)] for y in range(0, 3)]    
    
    gamer = random.randint(0, 10) % 2   #случайно выбираем кто ходит первым (первый ход -  "X")
    
    PlayerSign = [] # кодируем знаки ("X", "0") у игроков
    if gamer == 0:
        PlayerSign = [1, 2] #первым ходит игрок 0 => 0 : "X" (1) 1 : "0" (2)
    else:
        PlayerSign = [2, 1] #первым ходит игрок 1 => 0 : "0" (2) 1 : "X" (1)

    print("\033[H\033[J") #очистка экрана        
    turn = 0 # число ходов
    while True:
        print(f"============== ход {turn + 1} ================")
        DrawBoard(board)
        if gamer and computer:
            ComputerMove(board, PlayerSign[gamer])
        else:
            HumanMove(board, PlayerSign[gamer], Names[gamer])            
        DrawBoard(board)
        turn += 1
        
        if CheckWin(board):
            print(f"Игрок {Names[gamer]} выиграл!")
            return
        if turn == 3*3:
            print("Ничья")
            return
        
        gamer = (gamer + 1) % 2 #Ход следующего игрока
        

#Ход человека        
def HumanMove(board : list, sign : int, name : str):
    while True:
        inp = input(f"Ход игрока {name}. Введите координаты X, Y через пробел. [0..2]: ")
        inp = str.split(inp)
        if len(inp) == 2:
            if board[int(inp[1])] [int(inp[0])] == 0:
                board[int(inp[1])] [int(inp[0])] = sign
                return
        print("Ошибка! Попробуйте снова...")    
  

#Ход компьютера
def ComputerMove(board, sign):
    while True:
        x =  random.randint(0, 2)
        y =  random.randint(0, 2)
        if board[y] [x] == 0:
                board[y] [x] = sign
                print(f"Ход компьютера: ({x}, {y}).")
                return
                

# отрисовка игровой доски
def DrawBoard(board : list):
    for y in board:
        st = ""
        for it in y:
            if it == 0:
                st += "| "
            elif it == 1:
                st += "|X"
            else:
                st += "|0"
        st += "|"
        print(st)
    
# Присваиваем имена игроков
def NamesInput(computer : bool):
    if computer:
        return [input("Введите имя игрока: "), "компьютер"]
    else:
        return [input("Введите имя 1 игрока: "), input("Введите имя 2 игрока: ")]    


# Проверка выигрышной ситуации
def CheckWin(board : list):
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] != 0  or board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False

    
#Игра с компьютером    
Game(True)

#Игра с человеком
Game(False)
