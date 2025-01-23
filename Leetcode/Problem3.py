class Solution:
   def removeElement(self, nums , val) : 
      pos = 0
      for i in range(len(nums)):
         if nums[i] != val :
            nums[pos] = nums[i]
            pos = pos + 1
      return nums[:pos],len(nums)-pos
     

play = Solution()
l = [3,2,2,3,3,3,4,4,5,5]
print(len(l))
arr , count = play.removeElement(l,3)
print(arr,count)