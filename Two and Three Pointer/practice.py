# def TwoPointer(nums,x):
#     n = len(nums)
#     j = n-1
#     i = 0 

    while i < j :
        if nums[i] + nums[j] == x : 
            return True 
        
        if nums[i]+nums[j] < x :
            i = i + 1 
        else:
            j = j - 1 

    return False 

# print(TwoPointer([10,20,30,40],70))
s = "Dhaiya"
s = s.lower()

