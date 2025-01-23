import numpy as np 

def Get_Zero_Index(Grid):
    for i , row in enumerate(Grid):
        print(i,row)
        if 0 in row:
            return (i,row.index(0))
    return None 

def Is_Goal(Grid,Goal):
    return Grid == Goal 

def Generate_new_states(Grid):
    row , col = Get_Zero_Index(Grid)

    Direction = [(0,1),(1,0),(0,-1),(-1,0)] 
    New_States = []
    for dr , dc in Direction:
        new_row = dr + row # 1
        new_col = dc + col # 2 
        if 0 <= new_row < 3 and 0 <= new_col < 3 : # boundary 
            New_Grid = [row[:] for row in Grid] 
            New_Grid[row][col] , New_Grid[new_row][new_col] = New_Grid[new_row][new_col] , New_Grid[row][col]
            New_States.append(New_Grid)
    return New_States


def Depth_First_Search(Grid,Goal):
    Stack = [(Grid,[])] # states 
    seen = set()

    while Stack:
        current , path = Stack.pop()

        if Is_Goal(current,Goal):
            return path + [current]
        
        tup = tuple(tuple(t) for t in current) # 2d matrix into tuple 
        if tup in seen:
            print(f"Already seen state: {tup}")
            continue
        seen.add(tup)

        for Next_States in Generate_new_states(current):
            Next_State_tuple = tuple(tuple(r) for r in Next_States)
            if Next_State_tuple not in seen:
                Stack.append((Next_States,path+[current]))
    return None



if __name__ == '__main__':
    Start = [[1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]
            ]

    Goal = [[1,2,3],
            [4,5,6],
            [7,8,0]
                ]
    
    ans = Depth_First_Search(Start,Goal)
    for i , state in enumerate(ans):
        print(f'Step : {i+1}')
        print(f'\n{np.array(state)}')

