def Matrix_spiral(n):
    x = 0 
    y = 0 
    center = 0 
    num = 0
    dp = [[0]*n for _ in range(n)]
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    while num < n*n:
       if dp[x][y] == 0:
           num = num + 1 
           dp[x][y] = num
       dx = x + d[center][0]
       dy = y + d[center][1]
       if 0 <= dx < n and 0 <= dy < n and dp[dx][dy] == 0 :
          x,y = dx , dy 
       else:
        center = (center+1)%4
    return dp    


dp = Matrix_spiral(3)
print(dp)
