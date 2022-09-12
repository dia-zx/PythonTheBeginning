# Создайте программу для игры в ""Крестики-нолики"".

def Game(computer : bool):
    Names = NamesInput(computer)    
    

def DrawBoard(board : list):
    None
    
# Присваиваем имена игроков
def NamesInput(computer : bool):
    if computer:
        return [input("Введите имя игрока: "), "компьютер"]
    else:
        return [input("Введите имя 1 игрока: "), input("Введите имя 2 игрока: ")]    