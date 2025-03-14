class RecentCounter:

    def __init__(self):
        self.counter=[]

    def ping(self, t: int) -> int:
        self.counter.append(t)
        length=len(self.counter)
        range_st=t-3000
        if range_st<=self.counter[0]:
            return length

        left=0
        right=length-1
        while left<right:
            mid=(left+right)//2
            mid_value=self.counter[mid]
            if mid_value>=range_st:
                right=mid
            else:
                left=mid+1
        return length-left



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)