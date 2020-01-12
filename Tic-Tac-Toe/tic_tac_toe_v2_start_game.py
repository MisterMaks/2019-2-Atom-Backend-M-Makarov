"""Запуск игры Крестики-Нолики"""

from tic_tac_toe_v2 import TicTacToe


def start_game():
    """Запуск игры Крестики-Нолики"""

    return TicTacToe().game()


START = start_game()
