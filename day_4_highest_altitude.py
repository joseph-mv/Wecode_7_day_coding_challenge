from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Finds the highest altitude reached during a road trip.
        """
        high_alt=0
        alt=0
        for num in gain :
            alt+=num
            high_alt=max(high_alt,alt)
        return high_alt