# problem - 1  
# def fibo(n,dp):
#     if n <= 1 :
#         return n 
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = fibo(n-1,dp)+fibo(n-2,dp)
#     return dp[n]

# if __name__ == "__main__":
#     n = 10
#     dp = [-1] * (n+1)
#     print(fibo(n,dp)) 

# problem - 2

def min_path(cost,row,col,dp):

    if row >= 3 or col >= 3:
        return float('inf')
    
    if row == 2 and col == 2:
        return cost[row][col]
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    


    
        

    