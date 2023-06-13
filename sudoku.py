def is_input_valid(row_str):
    if len(row_str) != 9:
        print("Row length not equal to 9!")
        return False

    for i in row_str:
        if not i.isdigit():
            print("Invalid characters found in row!")
            return False

    return True


def get_user_input():

    puzzle = []
    for j in range(9):

        while True:
            row_str = input(f'Enter row number {j+1}: ')
            if is_input_valid(row_str.strip()):
                break

        row = [int(n) for n in list(row_str)]
        puzzle.append(row)

    return puzzle


def is_cell_correct(puzzle, i, j):
    value = puzzle[i][j]

    # checking row
    cur_row = puzzle[i]
    if value != 0 and cur_row.count(value) > 1:
        return False

    # checking column
    cur_col = []
    for row_index in range(9):
        cur_col.append(puzzle[row_index][j])

    if value != 0 and cur_col.count(value) > 1:
        return False

    # checking box
    box_i = i//3
    box_j = j//3
    box_i_start = box_i * 3
    box_j_start = box_j * 3
    cur_box = []
    for a in range(box_i_start, box_i_start+3):
        for b in range(box_j_start, box_j_start+3):
            cur_box.append(puzzle[a][b])
    if value != 0 and cur_box.count(value) > 1:
        return False

    return True


def is_puzzle_correct(puzzle):
    for i in range(9):
        for j in range(9):
            if not is_cell_correct(puzzle, i, j):
                return False

    return True


def find_empty_cell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None


def solve(puzzle):
    empty_cell = find_empty_cell(puzzle)

    if empty_cell is None:
        return True

    i, j = empty_cell

    for num in range(1, 10):
        puzzle[i][j] = num
        if is_cell_correct(puzzle, i, j):
            if solve(puzzle):
                return True

        puzzle[i][j] = 0

    return False


def print_puzzle(puzzle):
    for i in puzzle:
        print(i)


def main():
    puzzle = get_user_input()

    if not is_puzzle_correct(puzzle):
        print("Invalid Puzzle")
        return

    solve(puzzle)
    print_puzzle(puzzle)


if __name__ == '__main__':
    main()
