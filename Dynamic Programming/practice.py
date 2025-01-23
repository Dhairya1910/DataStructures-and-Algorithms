import numpy as np 
m = 2 
n = 3 
dp = [[-1 for i in range(n)] for j in range(m)]
def dfs(row,col):

    if row > m-1 or col > n-1:
        print("Row limit exceded")
        print(row,col)
        return 0 
    
    if dp[row][col] != -1 :
        return dp[row][col]
    
    if row == m-1 and col == n-1:
        print("col val = ",col)
        return 1

    print("Before : ",row,col)
    right_path = dfs(row+1,col)
    print("Here after : right path ",col)
    down_path = dfs(row,col+1)

    dp[row][col] =  right_path + down_path 
    print(f"At index ({row},{col}) = {right_path} + {down_path} =  {right_path+down_path}")
    return dp[row][col]
print(dfs(0,0))
print("-------------")
print(np.array(dp))


    
