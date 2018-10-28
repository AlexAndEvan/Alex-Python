from enum import Enum
from copy import deepcopy

log_message = False
def log(message):
    if log_message:
        print(message)

class BlockData:
    row_unused_numbers = set()
    column_unused_numbers = set()
    block_unused_numbers = set()
    cell_unused_numbers = set()
   
full_set = set(range(1, 10))

class SudokuSolver:
    @staticmethod
    def solve_sudoku(sudoku):
        local_copy = deepcopy(sudoku)
        log("deep copy input sudoku:")
        log(local_copy)
        block_data_map = SudokuSolver.analyze_sudoku(local_copy)
        if len(block_data_map) == 0:
            print('Solved:')
            SudokuSolver.print_result(local_copy)
            return True
        
        sorted_block_data_list = sorted(block_data_map.items(), key=lambda kv: len(kv[1].cell_unused_numbers)) 
        
        # We end up with a cell that have no number available to assign to it, deadend -- backtrack
        if len(sorted_block_data_list[0][1].cell_unused_numbers) == 0:
            log('Backtrack...')
            return False
        
        (i, j) = sorted_block_data_list[0][0]
        block_data = sorted_block_data_list[0][1]
        choose_number_from = list(block_data.cell_unused_numbers)
        for number_to_fill in choose_number_from:
            log('choose a number from:' + str(choose_number_from))
            log('Set value for (' + str(i) + ', ' + str(j) + '): ' + str(number_to_fill))
            #set the number to fill in cell (i, j)
            local_copy[i][j] = number_to_fill
            if SudokuSolver.solve_sudoku(local_copy):
                return True
        # We tried all possible numbers and still can not find a solution
        return False
    
    @staticmethod
    def analyze_sudoku(sudoku):
        block_data = {}
        #process row data
        row_index = 0
        while row_index < 9:
            i = 0
            empty = []
            used = set()
            while i < 9:
                if sudoku[row_index][i] == 0:
                    empty.append(i)
                else:
                    used.add(sudoku[row_index][i])
                i += 1
            unused_numbers = full_set.difference(used)
            for k in empty:
                block_data[(row_index, k)] = BlockData()
                block_data[(row_index, k)].row_unused_numbers = unused_numbers
            row_index += 1
        if len(block_data) == 0:
            return block_data
        #process column data
        column_index = 0
        while column_index < 9:
            i = 0
            empty = []
            used = set()
            while i < 9:
                if sudoku[i][column_index] == 0:
                    empty.append(i)
                else:
                    used.add(sudoku[i][column_index])
                i += 1
            unused_numbers = full_set.difference(used)
            for k in empty:
                block_data[(k, column_index)].column_unused_numbers = unused_numbers
            column_index += 1
        #process block data
        row_index = 0
        while row_index < 3:
            column_index = 0
            while column_index < 3:
                i = row_index * 3
                empty = []
                used = set()
                while i < (row_index + 1) * 3:
                    j = column_index * 3
                    while j < (column_index + 1) * 3:
                        if sudoku[i][j] == 0:
                            empty.append((i, j))
                        else:
                            used.add(sudoku[i][j])
                        j += 1
                    i += 1
                unused_numbers = full_set.difference(used) 
                for k in empty:
                    block_data[k].block_unused_numbers = unused_numbers
                column_index += 1
            row_index += 1
        for key, value in block_data.items():
            value.cell_unused_numbers = value.row_unused_numbers.intersection(\
                value.column_unused_numbers, value.block_unused_numbers)
        return block_data   

    @staticmethod
    def print_result(sudoku):
        for row in sudoku:
            print(row)
        print('------------------------------')