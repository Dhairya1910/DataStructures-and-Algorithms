# Implementation of 2D matrix Traversal using Graph in Python 
from collections import deque

Dir_Row = [-1,0,1,0]
Dir_Col = [0,1,0,-1]


def Breath_First_Search(Grid,row,col):
    queue = deque()
    Seen = set()
    queue.append((row,col))
    Seen.add((row,col))
    while queue:
        curr = queue.popleft()
        x = curr[0]
        y = curr[1]
        print(Grid[x][y])
        for i in range(4):
            adjx = x + Dir_Row[i]
            adjy = y + Dir_Col[i]
            if 0 <= adjx < len(Grid) and 0 <= adjy < len(Grid[0]) and (adjx, adjy) not in Seen:
                    queue.append((adjx,adjy))
                    Seen.add((adjx,adjy))

grid= [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ] ]

Breath_First_Search(grid,0,0)