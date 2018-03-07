import testCase
from Sudoku import *
from testCase import *


class SudokuTest(testCase.TestCase):
    def __init__(self):

        self.asserter = None
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
        for i in range(9):
            for j in range(9):
                if game.locked_numbers[i][j]:
                    self.asserter.assertFalse(game.change_number(i, j, 1), msg='change a locked number succeeded')
                    self.asserter.assertEquals(game.puzzle[i][j], puzzle[i][j])
                else:
                    self.asserter.assertTrue(game.change_number(i, j, i), msg="initial check failed")
                    self.asserter.assertEquals(game.puzzle[i][j], i)
                    self.asserter.assertTrue(game.change_number(i, j, 0), msg="initial check failed")
                    self.asserter.assertEquals(game.puzzle[i][j], puzzle[i][j])


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
        self.asserter.assertTrue(game.searches[0].isValid)
        game.change_number(0,2,3)
        game.check_area(0)
        self.asserter.assertFalse(game.searches[0].isValid)

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
        self.asserter.assertFalse(game.check_for_win())
        for i in range(9):
            for j in range(9):
                game.puzzle[i][j] = 1
        self.asserter.assertTrue(game.check_for_win())

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
        self.asserter.assertTrue(game.check_results([1,2,3]))
        self.asserter.assertFalse(game.check_results([15,2,3]))

if __name__ == '__main__':
    test = SudokuTest()
    test.run()