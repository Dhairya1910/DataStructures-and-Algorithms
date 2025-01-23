import math

# Define the Tic-Tac-Toe board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a win or tie
def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for tie
    for row in board:
        if ' ' in row:
            return None  # Game is still ongoing

    return 'Tie'  # No winner and no empty spaces = tie

# Function to check if there are any moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    # If the computer wins, return 10
    if winner == 'X':
        return 10 - depth
    # If the human wins, return -10
    elif winner == 'O':
        return depth - 10
    # If it's a tie, return 0
    elif winner == 'Tie':
        return 0
    
    # Maximizing player (computer's turn)
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    # Minimizing player (human's turn)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

# Function to find the best move for the computer
def find_best_move(board):
    best_move = (-1, -1)
    best_score = -math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_score = minimax(board, 0, False)
                board[i][j] = ' '

                if move_score > best_score:
                    best_move = (i, j)
                    best_score = move_score
    
    return best_move

# Function for the human player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Invalid move, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are O and the computer is X.")
    print_board(board)
    
    while True:
        # Human's turn
        player_move(board)
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        # Computer's turn
        print("Computer's move:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

# Start the game
play_game()
