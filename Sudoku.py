# Map the SUDOKU Matrix below
# Replace BLANK spaces with 0
grid = [[6, 0, 3, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 6, 0, 0, 0, 4, 0],
        [0, 9, 2, 0, 0, 0, 6, 0, 1],
        [0, 0, 0, 3, 0, 6, 7, 0, 0],
        [0, 5, 4, 0, 0, 0, 2, 6, 0],
        [0, 0, 7, 5, 0, 8, 0, 0, 0],
        [7, 0, 9, 0, 0, 0, 4, 5, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 7],
        [0, 0, 0, 0, 0, 7, 3, 0, 6]]


# Print the grid in SUDOKU format
def print_grid(g):
    for i in range(len(g)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(g)):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(g[i][j])
            else:
                print(str(g[i][j]) + " ", end="")


# Return the position of BLANK spaces
def find_zero(g):
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 0:
                return i, j

    return None


# Check all the Possibilities for a number to fit in
def possible(g, num, axis):
    # Check Horizontally
    for i in range(len(g)):
        if g[axis[0]][i] == num and axis[1] != i:
            return False

    # Check Vertically
    for i in range(len(g)):
        if g[i][axis[1]] == num and axis[0] != i:
            return False

    # Check Child Grid
    grid_x = axis[1] // 3
    grid_y = axis[0] // 3

    for i in range(grid_y * 3, grid_y * 3 + 3):
        for j in range(grid_x * 3, grid_x * 3 + 3):
            if g[i][j] == num and (i, j) != axis:
                return False

    return True


# Final Solution
def final_sol(g):
    find = find_zero(g)
    if not find:
        return True
    else:
        x, y = find

    for i in range(1, len(g) + 1):
        if possible(g, i, (x, y)):
            g[x][y] = i

            if final_sol(g):
                return True

            g[x][y] = 0

    return False


print("****** SUDOKU *******")
print("`````````````````````")
print_grid(grid)
final_sol(grid)
print("                     ")
print("***** SOLUTION ******")
print("`````````````````````")
print_grid(grid)
