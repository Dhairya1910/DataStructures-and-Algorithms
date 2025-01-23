import numpy as np 
from collections import deque

def get_zero_index(Grid):
    for i , row in enumerate(Grid):
        if 0 in row : 
            return (i , row.index(0))
    return None 

def Generate_new_States(Grid):
    row , col = get_zero_index(Grid)
    new_states = []
    Direction = [(0,1),(1,0),(-1,0),(0,-1)]
    for dr , dc in Direction:
        new_row = dr + row 
        new_col = dc + col 
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_grid = [list(row) for row in Grid]
            new_grid[row][col] , new_grid[new_row][new_col] = new_grid[new_row][new_col] , new_grid[row][col]
            new_states.append(new_grid)
    return new_states

def is_Goal_State(grid,goal):
    return grid == goal 

def Breadth_First_Search(Grid,goal):
    queue = deque([(Grid,[])])
    seen = set()
    while queue:
        current , path = queue.popleft()

        if is_Goal_State(current,goal):
            return path + [current]
        
        tup = tuple(tuple(t) for t in current)
        if tup in seen:
            continue
        seen.add(tup)

        for next_states in Generate_new_States(current):
            queue.append((next_states , path + [current]))

    return None
        
Start = [[1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
        ]

Goal = [[1,2,3],
        [4,5,6],
        [7,8,0]
            ]

ans = Breadth_First_Search(Start,Goal)

for i , grid in enumerate(ans):
    print(f'Step : {i+1} \n')
    print(np.array(grid),"\n")

