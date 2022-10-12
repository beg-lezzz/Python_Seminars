import random


def options_for_game():
    print('\n' + '*' * 15 + ' Основные настройки игры ' + '*' * 15 + '\n')
    player_1, player_2 = input('Введите имя Игрока 1: '), input('Введите имя Игрока 2: ')
    x_player = player_1 if random.randint(1, 2) == 1 else player_2
    o_player = player_1 if x_player == player_2 else player_2
    print('\n' + '*' * 19 + ' Начало игры ' + '*' * 19 + '\n')
    print("\033[33m{}".format('Начинает Игрок "{}". Ему выпало играть " Х "'.format(x_player)) + "\033[0m{}".format(''))
    return list(range(1, 10)), x_player, o_player


def print_game_field(game_field):
    print('\t')
    for i in range(3):
        print(" ", game_field[i * 3], " | ", game_field[1 + i * 3], " | ", game_field[2 + i * 3])
        print("-" * 17) if i < 2 else print('\t')


def player_turns(player_sign, game_field, x_player, o_player):
    flag = True
    current_player = x_player if player_sign == 'X' else o_player
    while flag:
        player_turn = input("Укажите, в какую клетку поставить " + player_sign + ", " + current_player + ": ")
        try:
            player_turn = int(player_turn)
        except ValueError:
            print("Ошибка. Введите число от 1 до 9")
            continue
        if 1 <= player_turn <= 9:
            if str(game_field[player_turn - 1]) not in "XO":
                game_field[player_turn - 1] = player_sign
                flag = False
            else:
                print("Эта клатка занята. Выберите другую.")
        else:
            print("Ошибка. Введите число от 1 до 9")


def check_win(game_field):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for combination in win_combinations:
        if game_field[combination[0]] == game_field[combination[1]] == game_field[combination[2]]:
            return game_field[combination[0]]
    return False


def main(input_data):
    counter = 0
    while True:
        print_game_field(input_data[0])
        player_turns("X", input_data[0], input_data[1], input_data[2]) if counter % 2 == 0 else\
            player_turns("O", input_data[0], input_data[1], input_data[2])
        counter += 1
        if counter > 4:
            winner = check_win(input_data[0])
            if winner:
                current_player = input_data[1] if winner == 'X' else input_data[2]
                print("\033[32m{}".format('\n' + current_player + ' победил! Он играл "' + winner + '"') +
                      "\033[0m{}".format(''))
                break
        if counter == 9:
            print("\033[32m{}".format("Победила дружба!"))
            break
    print_game_field(input_data[0])


main(options_for_game())
