arr = [1,2,3,4]
sol = []
res = []

def backtrack(x):
    if x == len(sol):
        res.append(sol[:])
        return 
    
    backtrack(x+1)
    
    sol.append(arr[x])
    backtrack(x+1)
    sol.pop()

backtrack(0)
print(res)
