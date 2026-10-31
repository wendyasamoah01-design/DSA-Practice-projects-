def find_empty(grid):
    
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)  
            
    return None

def is_valid(grid, guess, row, col):
    
    for i in range(9):
        if grid[row][i] == guess:
            return False
        
    for i in range(9):
        if grid[i][col] == guess:
            return False
        
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for i in range(row_start, row_start + 3): 
        for j in range(col_start, col_start + 3):
            
            if grid[i][j] == guess:
                return False
            
    return True

def solve_sudoku(grid):
    empty = find_empty(grid)
    
    if not empty:
        return True
    
    row, col = empty
    
    for guess in range(1, 10):
        if is_valid(grid, guess, row, col):
            grid[row][col] = guess
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0
        
    return False


grid=[
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7, 8]
]   #This sudoku has no solution. The program will return "No solution exists."        

# grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]  

if solve_sudoku(grid):
     print("Sudoku solved successfully!") 
     
     for row in grid:
         print(row)
         
else:
    print("No solution exists.")
               
    