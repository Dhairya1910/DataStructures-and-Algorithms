import heapq

def get_zero_index(puzzle, value):
    for i, row in enumerate(puzzle):
        if value in row:
            return i, row.index(value)
        
def Misplaced(puzzle, goal):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j]!=goal[i][j]:
                misplaced_tiles+=1
    return misplaced_tiles

def Gen_new_States(puzzle):
    New_states = []
    x, y = get_zero_index(puzzle, 0) 
    Direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for new_x, new_y in Direction:
        pos_x = x + new_x
        pos_y = y + new_y
        if 0 <= pos_x < 3 and 0 <= pos_y < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[x][y], new_puzzle[pos_x][pos_y] = new_puzzle[pos_x][pos_y], new_puzzle[x][y]
            New_states.append(new_puzzle)
    return New_states

def puzzle_to_tuple(puzzle):
    return tuple(tuple(row) for row in puzzle)

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, 0))
    g_score = {puzzle_to_tuple(start): 0}
    came_from = {}

    while open_list:
        f_score, current, current_g_score = heapq.heappop(open_list)
        if current == goal:
            path = []
            while puzzle_to_tuple(current) in came_from:
                path.append(current)
                current = came_from[puzzle_to_tuple(current)]
            path.append(start)
            return path[::-1] 
        
        for neighbor in Gen_new_States(current):
            neighbor_tuple = puzzle_to_tuple(neighbor)
            tentative_g_score = current_g_score + 1 

            if neighbor_tuple not in g_score or tentative_g_score < g_score[neighbor_tuple]:
                g_score[neighbor_tuple] = tentative_g_score
                f_score = tentative_g_score + Misplaced(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor, tentative_g_score))
                came_from[neighbor_tuple] = current

    return None 

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  
]

Ans = astar(start_state, goal_state)

for step, state in enumerate(Ans):
    print("\nStep", step)
    for row in state:
        print(row)

