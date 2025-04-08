SIZE=9

def last_remaining_cell(grid):
    update=True

    while update:
        update=False
        candidates=possible_number_inference(grid)
        if process_naked_singles(grid):
            update=True
            continue
        if process_hidden_singles_box(grid):
            update=True
            continue
        if process_hidden_singles_row(grid):
            update=True
            continue
        if process_hidden_singles_col(grid):
            update=True
            continue


def process_naked_singles(grid):
    candidates=possible_number_inference(grid)
    update=False
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0 and len(candidates[i][j]) == 1:
                grid[i][j] = candidates[i][j].pop()
                update = True
                break
    return update

def process_hidden_singles_row(grid):
    candidates=possible_number_inference(grid)
    update=False
    for i in range(SIZE): #对于每一行
        num_count = {num: [] for num in range(1, 10)} #记录行中每一格的候选集
        for j in range(SIZE): #对于行中每一个格子
            if grid[i][j] == 0:
                for num in candidates[i][j]:
                    num_count[num].append(j) #载入候选集
        for num in num_count:
            if len(num_count[num]) == 1:
                j = num_count[num].pop()
                if grid[i][j] == 0:
                    grid[i][j] = num
                    update = True
                    break
    return update

def process_hidden_singles_col(grid):
    candidates=possible_number_inference(grid)
    update=False
    for j in range(SIZE):
        num_count = {num: [] for num in range(1, 10)}
        for i in range(SIZE):
            if grid[i][j] == 0:
                for num in candidates[i][j]:
                    num_count[num].append(i)
        for num in num_count:
            if len(num_count[num]) == 1:
                i = num_count[num].pop()
                if grid[i][j] == 0:
                    grid[i][j] = num
                    update = True
                    break
    return update

def process_hidden_singles_box(grid):
    candidates=possible_number_inference(grid)
    update=False
    for box_row in range(0, SIZE, 3):
        for box_col in range(0, SIZE, 3):
            num_count = {num: [] for num in range(1, 10)}
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if grid[i][j] == 0:
                        for num in candidates[i][j]:
                            num_count[num].append((i, j))
            for num in num_count:
                if len(num_count[num]) == 1:
                    i, j = num_count[num].pop()
                    if grid[i][j] == 0:
                        grid[i][j] = num
                        update = True
                        break
    return update

def check_add_or_not(grid, row, col, num):
    start_row=(row//3)*3
    start_col=(col//3)*3
    for i in range(SIZE):
        if grid[row][i]==num or grid[i][col]==num:
            return False
    for i in range(3):
        for j in range(3):
            r=start_row+i
            c=start_col+j
            if (r,c)!=(row,col) and grid[r][c]==num:
                return False
    return True

def possible_number_inference(grid):
    candidates=[[set() for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if check_add_or_not(grid, i, j, num):
                        candidates[i][j].add(num)
    return candidates

def print_sudoku(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            print(grid[i][j], end=' ')
        print()

sudoku=[
    [0,0,5,7,1,9,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0],
    [0,5,0,0,2,0,7,0,6],
    [0,0,0,0,9,0,1,0,0],
    [3,0,0,0,0,0,2,5,0],
    [0,6,4,5,0,1,0,0,7],
    [8,1,0,0,0,3,0,0,5],
    [0,0,0,0,0,2,0,4,0]
]

last_remaining_cell(sudoku)
print_sudoku(sudoku)
