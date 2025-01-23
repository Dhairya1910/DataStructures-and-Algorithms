# class Solution:
#     def permuteUnique(self, nums):
#         def backtrack(arr, ds, res, hashmap):
#             if len(ds) == len(arr):
#                 if ds[:] not in res:
#                     res.append(ds[:])
#                 return

#             for i in range(len(arr)):
#                 if hashmap[i] == 1:
#                     continue
#                 hashmap[i] = 1
#                 ds.append(arr[i])
#                 backtrack(arr, ds, res, hashmap)
#                 ds.pop()
#                 hashmap[i] = 0

#         res = []
#         hashmap = [0]*len(nums)
#         backtrack(nums, [], res, hashmap)
#         return res


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


