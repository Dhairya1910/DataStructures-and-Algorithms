word = "ABCCE"
board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
n = len(board[0])  # Number of columns
m = len(board)     # Number of rows

def dfs(row, col, index, seen):
    # If the entire word is found
    if index == len(word):
        return True
    
    # Check bounds and constraints
    if not (0 <= row < m and 0 <= col < n):
        return False
    if (row, col) in seen or board[row][col] != word[index]:
        return False
    
    # Add current cell to the seen set
    seen.add((row, col))
    
    # Explore all 4 directions (right, down, left, up)
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if dfs(row + dr, col + dc, index + 1, seen):
            return True
    
    # Backtrack
    seen.remove((row, col))
    return False

# Wrapper function to find the word
def exist(board, word):
    for row in range(m):
        for col in range(n):
            if dfs(row, col, 0, set()):
                return True
    return False

# Check if the word exists in the board
print(exist(board, word))  # Output: False

    



