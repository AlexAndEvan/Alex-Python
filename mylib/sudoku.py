from enum import Enum

class BlockData:
    row_unused_numbers = set()
    column_unused_numbers = set()
    block_unused_numbers = set()
    cell_unused_numbers = set()
   
full_set = set(range(1, 10))

class Sudoku:

    def __init__(self, data):
        self.init_data = data
        self.result = data
        self.block_data = {}

        #process row data
        row_index = 0
        while row_index < 9:
            i = 0
            empty = []
            used = set()
            while i < 9:
                if data[row_index][i] == 0:
                    empty.append(i)
                else:
                    used.add(data[row_index][i])
                i += 1
            unused_numbers = full_set.difference(used)
            for k in empty:
                self.block_data[(row_index, k)] = BlockData()
                self.block_data[(row_index, k)].row_unused_numbers = unused_numbers
            row_index += 1
        #process column data
        column_index = 0
        while column_index < 9:
            i = 0
            empty = []
            used = set()
            while i < 9:
                if data[i][column_index] == 0:
                    empty.append(i)
                else:
                    used.add(data[i][column_index])
                i += 1
            unused_numbers = full_set.difference(used)
            for k in empty:
                self.block_data[(k, column_index)].column_unused_numbers = unused_numbers
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
                        if data[i][j] == 0:
                            empty.append((i, j))
                        else:
                            used.add(data[i][j])
                        j += 1
                    i += 1
                unused_numbers = full_set.difference(used) 
                for k in empty:
                    self.block_data[k].block_unused_numbers = unused_numbers
                column_index += 1
            row_index += 1
        for key, block_data in self.block_data.items():
            block_data.cell_unused_numbers = block_data.row_unused_numbers.intersection(\
                block_data.column_unused_numbers, block_data.block_unused_numbers)

    def solve_sudoku(self):
        while len(self.block_data) > 0:
            sorted_block_data = sorted(self.block_data.items(), key=lambda kv: len(kv[1].cell_unused_numbers)) 
            only_choices = list(filter(lambda x: len(x[1].cell_unused_numbers) == 1, sorted_block_data))
            if len(only_choices) > 0:
                self.update_blocK_data_for_only_choices(only_choices)
            else:
                print('Has to make guess now...')
                break
        if len(self.block_data) > 0:
            print('can not solve it without out guessing and backtracking... partial result:')
        for row in self.result:
            print(row)

    def update_blocK_data_for_only_choices(self, only_choices):
        for only_choice in only_choices:
            (i, j) = only_choice[0]
            block_data = only_choice[1]
            number_to_fill = list(block_data.cell_unused_numbers)[0]
            print('Find value for (' + str(i) + ', ' + str(j) + '): ' + str(number_to_fill))
            #set the number in cell (i, j)
            self.result[i][j] = number_to_fill
            self.block_data[(i,j)].row_unused_numbers.remove(number_to_fill)
            self.block_data[(i,j)].column_unused_numbers.remove(number_to_fill)
            self.block_data[(i,j)].block_unused_numbers.remove(number_to_fill)
            self.block_data.pop((i,j))
        for key, block_data in self.block_data.items():
            block_data.cell_unused_numbers = block_data.row_unused_numbers.intersection(\
                block_data.column_unused_numbers, block_data.block_unused_numbers)
