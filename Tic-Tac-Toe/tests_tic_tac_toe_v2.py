"""Тесты для tic_tac_toe"""

import unittest

from tic_tac_toe_v2 import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Класс тестов для tic_tac_toe"""

    def test_user_inputs(self):
        """Тесты для методов tic_tac_toe"""

        tic_tac_toe = TicTacToe()
        self.assertEqual(tic_tac_toe.check_tic_tac_toe_values("10"), "Error", 'Should be "Error"')
        self.assertEqual(tic_tac_toe.check_tic_tac_toe_values("b"), "Error", 'Should be "Error"')
        self.assertEqual(tic_tac_toe.check_tic_tac_toe_values("-1"), "Error", 'Should be "Error"')
        self.assertEqual(tic_tac_toe.check_tic_tac_toe_values("1.1"), "Error", 'Should be "Error"')
        self.assertEqual(tic_tac_toe.check_tic_tac_toe_values("qw12"), "Error", 'Should be "Error"')
        self.assertEqual(tic_tac_toe.check_tic_tac_toe_values("5"), 0, 'Should be 0')
        self.assertEqual(tic_tac_toe.check_empty_value(5), 0, 'Should be 0')
        self.assertIsNone(tic_tac_toe.input_value("5"), 'Should be None')
        self.assertEqual(tic_tac_toe.check_empty_value(5), "Error", 'Should be "Error"')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        self.assertIsNone(tic_tac_toe.input_value("1"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        self.assertIsNone(tic_tac_toe.input_value("7"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        self.assertIsNone(tic_tac_toe.input_value("4"), 'Should be None')
        self.assertIsNone(tic_tac_toe.input_value("3"), 'Should be None')
        self.assertEqual(tic_tac_toe.check_win(), "Victory", 'Should be "Victory"')
        tic_tac_toe = TicTacToe()
        self.assertIsNone(tic_tac_toe.input_value("1"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "O"
        self.assertIsNone(tic_tac_toe.input_value("2"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "X"
        self.assertIsNone(tic_tac_toe.input_value("3"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "O"
        self.assertIsNone(tic_tac_toe.input_value("5"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "X"
        self.assertIsNone(tic_tac_toe.input_value("4"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "O"
        self.assertIsNone(tic_tac_toe.input_value("7"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "X"
        self.assertIsNone(tic_tac_toe.input_value("6"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "O"
        self.assertIsNone(tic_tac_toe.input_value("9"), 'Should be None')
        self.assertIsNone(tic_tac_toe.check_win(), 'Should be None')
        tic_tac_toe.user_value = "X"
        self.assertIsNone(tic_tac_toe.input_value("8"), 'Should be None')
        self.assertEqual(tic_tac_toe.check_win(), "Game Over", 'Should be "Game Over"')
        self.assertEqual(tic_tac_toe.check_name("b"), 0, 'Should be 0')
        self.assertEqual(tic_tac_toe.check_name(""), "Error", 'Should be "Error"')
        self.assertEqual(tic_tac_toe.input_name("qwe"), "qwe", 'Should be "qwe"')


if __name__ == '__main__':
    unittest.main()
