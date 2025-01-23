# from collections import defaultdict 
# class Solution:
#     def fillBig(self,big):
#         return big  

#     def emptySmall(self):
#         return 0 
#     def Check(self , big , target , small):
#         if big == target or (big + small) == target or small == target:
#             small = 0
#             print(small,big)
#             return (small,big)
#         else:
#             print(small,big)

#     def TransferBigtoSmall(self,big,small,cap ,target):
#         if big + small <= cap:
#             small += big
#             big = 0
#         else:
#             big -= (cap - small)
#             small = cap
#         return big, small 


#     def canMeasureWater(self, x, y, target):
#         visited = defaultdict(lambda:False)
#         big = 0
#         small = 0
#         big_cap = max(x,y)
#         cap = min(x,y) 
#         if x + y == target:
#             return True
#         elif x==y :
#             return False
    
        

#         while(visited[(small,big)]==False):
#             big = self.fillBig(big_cap)
#             big , small = self.TransferBigtoSmall(big,small,cap,target)
#             if self.Check(big,target,small):
#                 return True
#             visited[(small,big)] = True
#             small = self.emptySmall()
#             big , small = self.TransferBigtoSmall(big,small,cap,target)  
#             if self.Check(big,target,small):
#                 return True 
#         print('not found')   
#         return False       

# print('small','big')
# A = Solution()
# A.canMeasureWater(3,2,1)


from collections import deque

class Solution:
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False
        if target == 0 or target == x or target == y or target == x + y:
            return True

        visited = set()
        queue = deque([(0, 0)]) # start state given 
        # A = 0 
        # B = 0 
        state = []
        while queue:
            a, b = queue.popleft()

            # a= 0 
            # b= 0
            
            if (a, b) in visited:
                continue
            visited.add((a,b))
            state.append((a,b))
            
            if a == target or b == target or a + b == target:
                print(f"Measured {target} units of water with ({a}, {b})")
                visited = list(visited)
                for j in state:
                    print("States : ",j)
                return True
            
            # Fill jug x
            queue.append((x, b)) # x = jug 1 water 
            # Fill jug y
            queue.append((a, y))
            # Empty jug x
            queue.append((0, b))
            # Empty jug y
            queue.append((a, 0))
            # Pour water from jug x to jug y
            queue.append((a - min(a, y - b), b + min(a, y - b)))
            # Pour water from jug y to jug x
            queue.append((a + min(b, x - a), b - min(b, x - a)))

        print("Cannot measure the target amount of water.")
        return False

A = Solution()
A.canMeasureWater(10, 8, 23)






        
        