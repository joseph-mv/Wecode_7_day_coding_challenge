class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_arr=list(s)
        vowels='aeiouAEIOU'

        left=0
        right=len(s_arr)-1

        while left<right:
            s_left=s_arr[left]
            s_right=s_arr[right]

            if s_left in vowels and s_right in vowels:
                [s_arr[left],s_arr[right]]=[s_arr[right],s_arr[left]] #swapping
                left+=1
                right-=1

            if s_left not in vowels:
                left+=1

            if s_right not in vowels:
                right-=1

        return ''.join(s_arr)

        