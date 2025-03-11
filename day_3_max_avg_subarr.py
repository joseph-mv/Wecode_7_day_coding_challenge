from typing import List

class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Find a contiguous subarray whose length is equal to k 
        that has the maximum average value and return this value.
        """
        max_total=sum(nums[:k])
        i=k

        total=max_total
        while i<len(nums):
            total=total+nums[i]-nums[i-k]
            max_total=max(max_total,total)
            i+=1

        return max_total/k