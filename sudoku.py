import random as rnd
import time
from math import sqrt, floor, ceil

# chooses random word from list of 20 hardest sudokus in line form
def choose_sudoku():
    with open('Sudoku_top20_hard.txt', 'r') as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = rnd.randrange(0, len(lines))
    return lines[line_number]

# turn the sudoku in 9x9 matrix
def grid_str(sudoku):
    sudoku = sudoku.replace('.', '0') # a '.' is replaced with '0' if present
    l = len(sudoku)  
    k = 0
    global sudoku_matrix
    row = floor(sqrt(l))
    column = ceil (sqrt(l))

    if (row * column < l):
        row = column

    sudoku_matrix= [[0 for j in range (column)] 
                       for i in range (row)]
    
    # convert the string into grid
    for i in range(row):
        for j in range(column):

            if k >= l:
                sudoku_matrix[i][j] = " "
                k += 1
                return sudoku_matrix
            else:
                sudoku_matrix[i][j] = int(sudoku[k])
                k += 1

# the array is turned into a 9x9 matrix as a redular sudoku
def print_matrix(sudoku_matrix):
    for i in range(9):
        for j in range(9):
            if sudoku_matrix[i][j] == " " :
                break
            print(sudoku_matrix[i][j], end = "")
        print()

# this searches the blank positions in the sudoku and stores them
def find_blanks(sudoku_matrix, blanks):
    for row in range(9):
        for col in range(9):
            if sudoku_matrix[row][col] == 0:
                blanks[0] = row
                blanks[1] = col
                return True
    return False

# solves the sudoku with a backtracking algorithm
def solve(sudoku_matrix):
    # list to store the empty postition
    blanks = [0, 0]
    # loop to find empty position
    if not find_blanks(sudoku_matrix, blanks):
        return True

    row = blanks[0]
    col = blanks[1]
    # the numbers from 1-9 are in consideration for the empty position
    for num in range(1,10):
        # it the empty position is okay the chosen number is filled in
        if(location_is_safe(sudoku_matrix, row, col, num)):
            sudoku_matrix[row][col] = num
            # loop for solving
            if(solve(sudoku_matrix)):
                return True
            # fills the position with '0' if num doesn't fit
            sudoku_matrix[row][col] = 0
    
    return False

# checks the limitations given by the sudoku rules
def location_is_safe(sudoku_matrix, row, col, num):
    return not used_in_row(sudoku_matrix, row, num) and not used_in_col(sudoku_matrix, col, num) and not used_in_box(sudoku_matrix, row - row%3, col - col%3, num)

# checks if the row is safe
def used_in_row(sudoku_matrix, row, num):
    for i in range(9):
        if(sudoku_matrix[row][i] == num):
            return True
    return False

# checks if the column is safe
def used_in_col(sudoku_matrix, col, num):
    for i in range(9):
        if(sudoku_matrix[i][col] == num):
            return True
    return False

# chechs if the 3x3 box is safe
def used_in_box(sudoku_matrix, row, col, num):
    for i in range(3):
        for j in range(3):
            if(sudoku_matrix[i+row][j+col] == num):
                return True
    return False

sudoku = choose_sudoku()
grid_str(sudoku)
start = time.perf_counter()
print_matrix(sudoku_matrix)
print('---------solving---------')
if(solve(sudoku_matrix)):
    print('solving the sudoku took ',time.perf_counter()-start,' seconds')
    print_matrix(sudoku_matrix)
else:
    print('not solvable')