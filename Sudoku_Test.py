import unittest
from Sudoku import *


class SudokuTest(unittest.TestCase):

    def test_change_number(self):
        puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        game = Sudoku(puzzle)
        self.assertTrue(game.change_number(0,2,2))
        self.assertFalse(game.change_number(0, 1, 2))
        self.assertEqual(game.puzzle[0][2], 2)
        self.assertEqual(game.puzzle[0][1],3)

    def test_check_area(self):
        puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        game = Sudoku(puzzle)
        self.assertTrue(game.searches[0].isValid)
        game.change_number(0,2,3)
        game.check_area(0)
        self.assertFalse(game.searches[0].isValid)

    def test_check_for_win(self):
        puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        game = Sudoku(puzzle)
        self.assertFalse(game.check_for_win())
        for i in range(9):
            for j in range(9):
                game.puzzle[i][j] = 1
        self.assertTrue(game.check_for_win())

    def test_check_results(self):
        puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        game = Sudoku(puzzle)
        self.assertTrue(game.check_results([1,2,3]))
        self.assertFalse(game.check_results([15,2,3]))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SudokuTest)
    unittest.TextTestRunner(verbosity=2).run(suite)