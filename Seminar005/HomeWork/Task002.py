import random


def options_for_game():
    print('\n' + '*' * 15 + ' Основные настройки игры ' + '*' * 15 + '\n')
    type_of_game = int(input('Введите тип игры (1 - два игрока, 2 - игра против "глупого" бота, 3 - игра против "умного" бота) : '))
    bot_name = 'Stupid_Bot' if type_of_game == 2 else 'Clever_Bot' if type_of_game == 3 else None
    count_of_candies = int(input('Введите количество конфет для игры: '))
    step_of_catch = int(input('Введите количество конфет, которое можно брать за 1 ход - от 1 до: '))

    if type_of_game == 1:
        player_1, player_2 = input('Введите имя Игрока 1: '), input('Введите имя Игрока 2: ')
    else:
        player_1, player_2 = input('Введите имя Игрока: '), bot_name

    current_player = player_1 if random.randint(1, 2) == 1 else player_2
    print('\n' + '*' * 19 + ' Начало игры ' + '*' * 19 + '\n')
    print("\033[33m{}".format('Начинает Игрок "{}".'.format(current_player)) + "\033[0m{}".format(''))

    return count_of_candies, step_of_catch, player_1, player_2, current_player, type_of_game


def two_players_game(count_of_candies, step_of_catch, player_1, player_2, current_player):
    while count_of_candies > 0:
        print('\n' + "\033[33m{}".format('Количесто конфет на столе => {} <='.format(count_of_candies)) + "\033[0m{}".format(''))
        step_of_catch = count_of_candies if count_of_candies < step_of_catch else step_of_catch
        while True:
            number_to_delete = int(input('Ход Игрока "{}" (1 - {}): '.format(current_player, step_of_catch)))
            if 1 <= number_to_delete <= step_of_catch:
                break
            else:
                print("\033[31m{}".format('Введите количество конфет от 1 до ' + str(step_of_catch)) +
                      "\033[0m{}".format(''))
        count_of_candies -= number_to_delete
        if count_of_candies != 0:
            current_player = player_2 if current_player == player_1 else player_1

    return '\n' + "\033[32m{}".format('Победил "{}"'.format(current_player)) + "\033[0m{}".format('')


def one_player_game(count_of_candies, step_of_catch, player_1, player_2, current_player, type_of_game):
    while count_of_candies > 0:
        print('\n' + "\033[33m{}".format('Количесто конфет на столе => {} <='.format(count_of_candies)) + "\033[0m{}".format(''))
        step_of_catch = count_of_candies if count_of_candies < step_of_catch else step_of_catch
        while True:
            if current_player == player_1:
                number_to_delete = int(input('Ход Игрока "{}" (1 - {}): '.format(current_player, step_of_catch)))
                if 1 <= number_to_delete <= step_of_catch:
                    break
                else:
                    print("\033[31m{}".format('Введите количество конфет от 1 до ' + str(step_of_catch)) +
                          "\033[0m{}".format(''))
            else:
                if type_of_game == 2:
                    number_to_delete = random.randint(1, step_of_catch) if count_of_candies > step_of_catch \
                        else count_of_candies
                else:
                    number_to_delete = count_of_candies % (step_of_catch + 1) if \
                        count_of_candies % (step_of_catch + 1) != 0 else count_of_candies if \
                        count_of_candies < step_of_catch else step_of_catch
                print('Ход Игрока "{}" (1 - {}): {}'.format(current_player, step_of_catch, number_to_delete))
                break
        count_of_candies -= number_to_delete
        if count_of_candies != 0:
            current_player = player_2 if current_player == player_1 else player_1

    return '\n' + "\033[32m{}".format('Победил "{}"'.format(current_player)) + "\033[0m{}".format('')


def start_game(input_list):
    if input_list[5] == 1:
        return two_players_game(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4])
    else:
        return one_player_game(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4], input_list[5])


print(start_game(options_for_game()))
