# Program for permutation
''' arr = [1,2,3]
sol = []
res = []

def BackTrack():
    if len(sol) == len(arr):
        res.append(sol[:])
        return 
    
    for i in range(len(arr)):

        if arr[i] in sol:
            continue 

        sol.append(arr[i])
        BackTrack()
        sol.pop()

BackTrack()
print(res)  '''

# Knights Tour problem 


import numpy as np

grid = [[False] * 8 for _ in range(8)]
chess_board = [[-1] * 8 for _ in range(8)]

def goal_state(moves):
    if moves == 64:
        return True
    else :
        return False
    
def Valid_moves(row,col):
    return 0<=row<8 and 0 <= col < 8 and not grid[row][col]
        
def make_move(row,col,moves):
    if goal_state(moves):
        print(np.array(chess_board))
        return True
    else:
         k_moves = [(2,1),(1,2),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
         for move in k_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if Valid_moves(new_row,new_col):
                grid[new_row][new_col] = True 
                chess_board[new_row][new_col] = moves

                if make_move(new_row,new_col,moves+1):
                     return True 
                
                grid[new_row][new_col] = False
                chess_board[new_row][new_col] = -1

    return False

grid[0][0] = True 
chess_board[0][0] = 0
print(make_move(0,0,1))




        

    
    