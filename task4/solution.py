def main():
    draws, bingo_boards = read_data()
    print(task1(draws, bingo_boards))


def task1(draws, bingo_boards):
    for draw in draws:
        for bingo_board in bingo_boards:
            for row in bingo_board:
                if draw in row:
                    row[row.index(draw)] = -1
                    if check_win(bingo_board):
                       return get_sum_of_unmarked_numbers(bingo_board) * draw
    return 0

def get_sum_of_unmarked_numbers(bingo_board):
    unmarked_sum = 0
    for row in bingo_board:
        row = [x if x != -1 else 0 for x in row]
        unmarked_sum += sum(row)
    return unmarked_sum

def check_win(bingo_board):
    for i, row in enumerate(bingo_board):
        row_sum = sum(row)
        col_sum = sum([r[i] for r in bingo_board])
        if row_sum == -5 or col_sum == -5:
            return True
    return False

def read_data():
    with open('input.txt') as file:
        input = file.read().splitlines()
    draws = [int(x) for x in input[0].split(",")]
    bingo_boards = []
    
    for i in range(len(input[2:])//6):
        bingo_boards.append(input[2+i*6:i*6+7])
    
    parsed_boards = []
    for board in bingo_boards:
        board = [row.split(" ") for row in board]
        board = [[int(x) for x in line if x != ""] for line in board]
        parsed_boards.append(board)
    return draws, parsed_boards
    
if __name__ == "__main__":
    main()