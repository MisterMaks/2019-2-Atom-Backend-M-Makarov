"""Игра Крестики-Нолики"""

from django.utils.termcolors import colorize


class TicTacToe:
    """Класс для игры в Крестики-Нолики"""

    def __init__(self):

        self.values = [i for i in range(1, 10)]
        self.winning_options = {"g": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                "v": [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
                                "d": [[1, 5, 9], [3, 5, 7]]}
        self.user_values = [colorize("X", fg='red'), colorize("O", fg='blue')]

        self.users = {}
        self.user_value = self.user_values[0]
        # self.game()

        self.check_syntax_shut_up = None

    def game(self):
        """Игра"""

        print("\n-----------------")
        print("|Крестики-нолики|")
        print("-----------------\n")

        print("Введите имя игрока, который будет играть {}".format(self.user_value))
        user_x = input()
        user_x = self.input_name(user_x)
        user_x = colorize(user_x, fg='red')
        print()

        self.user_value = self.user_values[1]
        print("Введите имя игрока, который будет играть {}".format(self.user_value))
        user_o = input()
        user_o = self.input_name(user_o)
        user_o = colorize(user_o, fg='blue')
        print()

        self.users = {self.user_values[0]: user_x, self.user_values[1]: user_o}

        self.print_table()

        self.user_value = self.user_values[0]

        print("\nГде будет {}?".format(self.user_value))
        user_input = input()
        self.input_value(user_input)
        print()

        i_for_change_user_value = 1
        while self.check_win() is None:
            self.print_table()
            self.user_value = self.user_values[i_for_change_user_value % 2]
            print("\nГде будет {}?".format(self.user_value))
            user_input = input()
            self.input_value(user_input)
            print()
            i_for_change_user_value += 1

        if self.check_win() == "Victory":
            self.print_table()
            print("\nПоздравляю {}: {} выиграли!!!\n".format(self.users[self.user_value],
                                                             self.user_value))

        elif self.check_win() == "Game Over":
            self.print_table()
            print("\nGame Over\n")

        print("Повторить? (Введите: 1 - если Да, Другое - если Нет)")
        user_ans = input()
        if user_ans == "1":
            self.__init__()
            self.game()
        else:
            print("\nGame Over\n")
            self.__init__()
        return None

    def input_value(self, user_input):
        """Принимает ввод пользователя, выполняет проверку, вставляет значения"""

        if self.check_tic_tac_toe_values(user_input) == "Error":
            print("\nError: '{}' - нет такой ячейки".format(colorize(user_input, bg="red")))
            print("Повторите ввод\n")
            self.print_table()
            print("Где будет {}?\n".format(self.user_value))
            return self.input_value(input())

        user_input = int(user_input)

        if self.check_empty_value(user_input) == "Error":
            print("\nТут уже занято")
            print("Повторите ввод\n")
            self.print_table()
            print("Где будет {}?\n".format(self.user_value))
            return self.input_value(input())

        self.values[user_input - 1] = self.user_value

        for key in self.winning_options:
            for id_option in range(len(self.winning_options[key])):
                for value_id in range(len(self.winning_options[key][id_option])):
                    if self.winning_options[key][id_option][value_id] == user_input:
                        self.winning_options[key][id_option][value_id] = self.user_value

        return None

    def print_table(self):
        """Печатает поле"""

        print("-------")
        for id_value in range(len(self.values)):
            print("|{}".format(self.values[id_value]), end="")
            if (id_value + 1) % 3 == 0:
                print("|")
                print("-------")

        return None

    def check_empty_value(self, user_input):
        """Проверяет что место свободно"""

        if self.values[user_input - 1] in self.user_values:
            return "Error"

        return 0

    def check_tic_tac_toe_values(self, user_input):
        """Проверяет ввод пользователя"""

        self.check_syntax_shut_up = None

        if user_input not in [str(i) for i in range(1, 10)]:
            return "Error"

        return 0

    def check_win(self):
        """Проверяет выигрыш"""

        for key in self.winning_options:
            for option in self.winning_options[key]:
                if [self.user_values[0]] * 3 == option or [self.user_values[1]] * 3 == option:
                    return "Victory"

        for value in self.values:
            if isinstance(value, int):
                return None

        return "Game Over"

    def check_name(self, name, print_mes=False):
        """Проверяет длину имени"""

        self.check_syntax_shut_up = None

        if name == "":
            if print_mes:
                print("\nError: вы не указали имя")
                print("Повторите ввод\n")
            return "Error"
        return 0

    def input_name(self, name):
        """Вставляет имя пользователя"""

        user_name = self.check_name(name, print_mes=True)
        if user_name == "Error":
            print("Введите имя игрока, который будет играть {}".format(self.user_value))
            return self.input_name(input())

        return name
