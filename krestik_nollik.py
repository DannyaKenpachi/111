from random import randint
def display_board(num):
    """Функция возращает нумерацию ячеек на игровом поле"""
    print('\n' + num[1] + '|' + num[2] + '|' + num[3])
    print('-|-|-')
    print(num[4] + '|' + num[5] + '|' + num[6])
    print('-|-|-')
    print(num[7] + '|' + num[8] + '|' + num[9] + '\n')

def player_input():
    """Функция определяет, кто ходит первый, и каким символом ходит игрок"""
    t = True
    ph = randint(1, 2)
    while t:
        test = input(f'Выбирает {ph} игрок. Крестик или нолик: ')
        if test == 'x' or test == '0':
            t = False
        else:
            print('Ошибка, попробуйте еще раз')
    return test, ph

def place_maker(board, marker, kto_perv, num):
    """Функция реализует ходы игроков по порядку"""
    poss = 0
    if num % 2 == 1 :
        if kto_perv == 1:
            poss = 2
        else:
            poss = 1
        if marker == 'x':
            marker = '0'
        else:
            marker = 'x'
    else:
        poss = kto_perv
    t = True
    while t:
        f = True
        while f:
            position = input(f'Ход игрока {poss}. Введите номер поля: ')
            if position not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                print('Ошибка, попробуйте еще раз')
            else:
                f = False
        if board[int(position)] in ('x', '0'):
            print('Ошибка, попробуйте еще раз')
        else:
            t = False
    board.pop(int(position))
    board.insert(int(position), marker)
    display_board(board)
    return board

def play(n, value_play, pole):
    """Функция проверяет, выйграл ли игрок или ничья. Если нет, то продолжает игру"""
    n = 0
    while n <= 9:
        result = winner(pole, n, value_play[1])
        if result != True and n < 9:
            place_maker(pole, value_play[0], value_play[1], n)
            n += 1
        else:
            n = 10
    if result is not True and n == 10:
        print('Ничья')
    print('Конец игры')
    restart()

def winner(board, num, value_play):
    """Функция проверяет, были ли реализованы выйгрышные случаи"""
    if board[1] == board[2] and board[1] == board[3] and board[1] in ('x', '0') or\
       board[4] == board[5] and board[4] == board[6] and board[4] in ('x', '0') or\
       board[7] == board[8] and board[7] == board[9] and board[7] in ('x', '0') or\
       board[1] == board[4] and board[1] == board[7] and board[1] in ('x', '0') or\
       board[2] == board[5] and board[2] == board[8] and board[2] in ('x', '0') or\
       board[3] == board[6] and board[3] == board[9] and board[3] in ('x', '0') or\
       board[1] == board[5] and board[1] == board[9] and board[1] in ('x', '0') or\
       board[3] == board[5] and board[3] == board[7] and board[3] in ('x', '0'):
        if num % 2 == 1:
            print(f'Выйграл {value_play} игрок')
        else:
            if value_play == 1:
                print('Выйграл 2 игрок')
            else:
                print('Выйграл 1 игрок')
        return True

def restart():
    """Функция реализует повтор игры, если надо"""
    f = input('Хотите еще раз? Введите да или нет: ').lower()
    while f not in ('да', 'нет'):
        print('Ошибка, повторите ввод')
        f = input('Хотите еще раз? Введите да или нет: ').lower()
    if f == 'да':
        print('')
        start_game()

def start_game():
    """Функция начала игры, которая включает в себя начальное поле, порядок ходя игроков и первый символ"""
    pole = list(' ' * 10)
    print('Добро пожаловать в игру - крестики, нолики\nПример нумерации поля:')
    display_board(list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))
    value_play = player_input()
    play(0, value_play, pole)

start_game()