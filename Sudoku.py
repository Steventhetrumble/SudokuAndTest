from __future__ import print_function
from colorama import Fore, Back, Style


class Sudoku():
    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.locked_numbers= []
        for i in range(len(self.puzzle)):
            temp = []
            for j in range(len(self.puzzle[0])):
                if self.puzzle[i][j] == 0:
                    temp.append(0)
                else:
                    temp.append(1)
            self.locked_numbers.append(temp)
        self.isValid = []
        for i in range(len(self.puzzle)):
            temp = []
            for j in range(len(self.puzzle[0])):
                temp.append(1)
            self.isValid.append(temp)
        self.searches = []
        for i in range(27):
            if i >= 0 and i < 9:
                TemplowRow = i % 9
                TemphighRow = i % 9
                TemplowCol = 0
                TemphighCol = 8
            elif (i >= 9 and i < 18):
                TemplowRow = 0
                TemphighRow = 8
                TemplowCol = i % 9
                TemphighCol = i % 9
            else:
                TemplowRow = (i % 9) / 3 * 3
                TemphighRow = (i % 9) / 3 * 3 + 2
                TemplowCol = (i % 3) * 3
                TemphighCol = (i % 3) * 3 + 2
            temp = SearchArea(TemplowRow, TemphighRow, TemplowCol, TemphighCol)
            self.searches.append(temp)

    def change_number(self,row,col,change):
        if self.locked_numbers[row][col]== 0:
            self.puzzle[row][col] = change
            return True
        else:
            return False

    def check_puzzle(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                self.isValid[i][j] = 1
        for i in range(len(self.searches)):
            self.check_area(i)

    def check_area(self, index):
        self.searches[index].isValid = True
        flag = []
        for i in range(9):
            flag.append(0)

        for i in range(self.searches[index].LowRow,self.searches[index].HighRow+1):
            for j in range(self.searches[index].LowCol,self.searches[index].HighCol+1):
                if self.puzzle[i][j] == 0:
                    continue
                elif (flag[self.puzzle[i][j]-1]== 1):
                    #print (Fore.CYAN + "error found at {},{}".format(i+1,j+1))
                    self.searches[index].isValid = False
                else:
                    flag[self.puzzle[i][j]-1]= 1
        if not self.searches[index].isValid:
            for i in range(self.searches[index].LowRow, self.searches[index].HighRow+1):
                for j in range(self.searches[index].LowCol, self.searches[index].HighCol+1):
                    self.isValid[i][j] = 0

    def display(self):
        for i in range(9):
            for j in range(9):
                if (self.isValid[i][j]):
                    if self.locked_numbers[i][j]:
                        print(Fore.LIGHTWHITE_EX + Back.GREEN + "{}".format(self.puzzle[i][j]), end=" ")
                    else:
                        print(Back.GREEN + "{}".format(self.puzzle[i][j]), end=" ")
                else:
                    if self.locked_numbers[i][j]:
                        print(Fore.LIGHTWHITE_EX+Back.RED + "{}".format(self.puzzle[i][j]), end=" ")
                    else:
                        print(Back.RED + "{}".format(self.puzzle[i][j]), end=" ")
            print(Back.LIGHTWHITE_EX)
        print(Back.LIGHTWHITE_EX)

    def check_for_win(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                if self.puzzle[i][j]==0 or self.isValid[i][j]== 0:
                    return False
        return True

    @staticmethod
    def check_results(results):
        for result in results:
            if result < 0 or result > 8:
                return False
        return True

    def main(self):
        print(Fore.BLUE + "Welcome to Sudoku!!")
        while (True):
            self.display()
            move = raw_input("Pleas enther the row, col, and change you would like to make : ")
            results = []
            for char in move:
                if char == " " or char == ",":
                    continue
                else:
                    try:
                        results.append(int(char) - 1)
                    except ValueError:
                        print(Fore.RED + "The following was an invalid entry: {}".format(char))
                        continue
            if len(results) != 3:
                print(Fore.RED + "You have entered the incorect number of arguments")
                continue
            if not self.check_results(results):
                print(Fore.RED + "please enter numbers between 1-9 inclusive")
                continue

            if self.change_number(results[0], results[1], results[2] + 1):
                self.check_puzzle()
                if self.check_for_win():
                    print("You Won!!")
                    break
                continue
            else:
                print(Fore.RED + "the starting numbers are locked and can not be modified")



class SearchArea():
    def __init__(self,LowRow,HighRow,LowCol, HighCol):
        self.LowRow = LowRow
        self.HighRow = HighRow
        self.LowCol = LowCol
        self.HighCol = HighCol
        self.isValid = True

'''
if __name__ == "__main__":
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
    game.main()
'''