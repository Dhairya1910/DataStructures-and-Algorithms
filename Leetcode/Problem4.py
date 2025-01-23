    class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums.reverse()
        if target > nums[0]:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        nums.sort()
        if target > nums[0]:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else: 
            nums.append(target)
            nums.sort()
            return nums.index(target)




