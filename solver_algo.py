def print_board(board):
    sub_board_len = int(len(board)**0.5)

    for i in range(len(board)):
        if i % sub_board_len == 0 and i != 0:
            print('- '* sub_board_len * 4)
        
        for j in range(len(board[0])):
            if j % sub_board_len == 0 and j != 0:
                print(' | ', end='')

            if j == len(board) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j


board =[  
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
       ] 
