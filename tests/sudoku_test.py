import unittest
import sys
import os
sys.path += ['..', '../..']
from AlexPython.mylib.sudoku import Sudoku

class TestStringMethods(unittest.TestCase):

    def test_sudoku(self):
        lines = self.read_data()
        i = 0
        index = 1
        while(i < 50):
            print(lines[index - 1])
            raw_data = lines[index:index+9]
            index += 10
            data = [[int(y) for y in list(x[:-1])] for x in raw_data]
            sudoku = Sudoku(data)
            sudoku.solve_sudoku()
            i += 1

    def read_data(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f = open(dir_path+'/sudoku.test.data', "r")
        lines = f.readlines()
        f.close()
        return lines

if __name__ == '__main__':
    unittest.main()