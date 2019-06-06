#Sea Battle mini - Console Application
#5x5 ships - 5 of 1
#■╳○
import random
boardlength = 5
ships = 10
def restart():
    game()
def create_board():
    board = []
    for i in range(boardlength):
        board.append(["○"] * boardlength)
    return board
def print_board(board):
    draw = ""
    for i in board:
        for l in i:
            draw += l
        draw += "\n"
    return draw
def set_ships(board):
    for i in range(ships):
        while True:
            x = random.randint(0,4)
            y = random.randint(0,4)
            if not board[y][x] == "■":
                board[y][x] = "■"
                break
def is_win(board):
    iswin = False
    for i in board:
        for l in i:
            if not l == "■":
                iswin = True
            else:
                iswin = False
                break
        if not iswin:
            iswin = False
            break
    return iswin
def shoot(board, x, y):
    ishit = False
    if board[y-1][x-1] == "■":
        ishit = True
    board[y-1][x-1] = "◉"
    return ishit
def game(ships):
    print("Игра Морской Бой 5х5")
    user_board = create_board()
    bot_board = create_board()
    set_ships(user_board)
    set_ships(bot_board)
    print(print_board(user_board))
    wrongs = []
    step = 1
    while not is_win(bot_board) and not is_win(user_board):
        if step == 1:
            while True:
                try:
                    x = int(input("Введи 1 координату от 1 до 5: "))
                    if x < 1 or x > 5:
                        print("Я тебя не понимаю!")
                        continue
                    else:
                        y = int(input("Введи 2 координату от 1 до 5: "))
                        if y < 1 or y > 5:
                            print("Я тебя не понимаю!")
                        else:
                            break
                except ValueError:
                    print("Я тебя не понимаю!")
            if shoot(bot_board, x, y):
                ships -= 1
                print("Ты попал! У противника осталось", ships,"кораблей!")
                step = 1
            else:
                print("Промазал!")
                step = 2
            if is_win(bot_board):
                print("Ты выиграл!")
        else:
            iswrong = False
            while True:
                x = random.randint(1, 5)
                y = random.randint(1, 5)
                if not wrongs == []:
                    for i in range(len(wrongs)):
                        if x == wrongs[i][0]:
                            if y == wrongs[i][1]:
                                iswrong = True
                                break
                        else:
                            iswrong = False
                    if not iswrong:
                        break
                else:
                    break
            if shoot(user_board, x, y):
                print("В тебя попали!")
                step = 2
                wrongs.append([x, y])
            else:
                print("Соперник прмахнулся!")
                step = 1
                wrongs.append([x, y])
            print(print_board(user_board))
            if is_win(user_board):
                print("Ты проиграл!")
    while True:
        isrestart = input("Хочешь поиграть ещё?(да/нет): ").lower()
        if isrestart == "да":
            print("Хорошо! Удачи!")
            restart()
        elif isrestart == "нет":
            print("Пока!")
            break
game(ships)