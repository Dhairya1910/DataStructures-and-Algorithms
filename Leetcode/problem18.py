class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        count = 0
        avl_flip = k
        greatest = 0
        for r in range(n):
            l = r
            count = 0 
            while l < n:
                if nums[l] == 1:
                    count += 1
                    l = l + 1
                elif nums[l] == 0 and avl_flip == 0:
                    count += 1
                    avl_flip -= 1
                    l = l + 1
                else:
                    break
                print(count)
            greatest = max(greatest, count)
        return greatest

A = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2 
Z = A.longestOnes(nums,k)
print(Z)