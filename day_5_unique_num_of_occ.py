from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
         Return true if the number of occurrences of each value in the array is unique or false otherwise.
        """
        hash={}
        for num in arr:
            hash[num]=( hash.get(num) or 0 ) +1
        
        hash_set=set()
        for count in hash.values():
            if count in hash_set:
                return False
            hash_set.add(count)
        return True