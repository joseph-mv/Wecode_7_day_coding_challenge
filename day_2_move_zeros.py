class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        count=0
        while count<len(nums):
            if nums[left]==0:
                del nums[left]
                nums.append(0)
            else:
                left+=1
            count+=1