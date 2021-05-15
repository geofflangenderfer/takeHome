#Output: 3
#n = 7
#          0,1,2,3,4,5,6,7
#ranges = [1,2,1,0,2,1,0,1]
#                        i
#interval = [-1,6]
#cur = [6,8]
#dp[0] = 1
#dp[1] = 1
#dp[2] = 1
#dp[3] = 1
#dp[4] = 2
#dp[5] = 2
#dp[6] = 2
#dp[7] = 3
#
#Output: 2
#n = 8
#          0,1,2,3,4,5,6,7,8
#ranges = [4,0,0,0,0,0,0,0,4]
#          i
#g      = [-4,4]
#cur    = [1,1]
#dp[0]  = 1
#dp[1]  = 
#dp[2]  = 
#dp[3]  = 
#dp[4]  = 
#dp[5]  = 
#dp[6]  = 
#dp[7]  = 
#dp[8]  = 
#
#expected = 1
#
#expected = 2
#            0,1,2,3,4,5,6,7,8
#ranges   = [4,0,0,0,0,0,0,0,4]
#              i
#g        = [-4,4]
#cur      = []
#dp[0]    = 1
#dp[1]    =
#dp[2]    =
#dp[3]    =
#dp[4]    =
#dp[5]    =
#dp[6]    =
from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        class Interval:
            def __init__(self,beg,end): self.beg,self.end = beg,end
            def __repr__(self):
                return f"[{self.beg},{self.end}]"

        def coverage(a: Interval) -> int:

            return a.end-a.beg
        def get_merged(a: Interval, b: Interval) -> Interval:
            if a.end == a.end: return b
            if b.end == b.end: return a
            beg = min(a.beg,b.beg)
            end = max(a.end,b.end)
            print(beg, end)
            print()
            return Interval(beg,end)

        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        g = Interval(0,0)#Interval(0-ranges[0], 0+ranges[0])
        for i in range(1,n+1):
            cur = Interval(i-ranges[i], i+ranges[i])
            if cur.beg <= g.beg and cur.end >= g.end:
                g = cur
                dp[i] = dp[i-1]
                print("hi")
                print(f" dp {dp} ranges[{i}] {ranges[i]} cur {cur} g {g}")
            else:
                merged = get_merged(cur,g)
                #print(f"{merged} {coverage(merged)} {g} {coverage(g)}")
                if coverage(merged) > coverage(g):
                    g = merged
                    dp[i] = dp[i-1] + 1
                    print(f" dp {dp} ranges[{i}] {ranges[i]} cur {cur} g {g} merged {merged}")
                else:
                    dp[i] = dp[i-1]
                    print(f" dp {dp} ranges[{i}] {ranges[i]} cur {cur} g {g} merged {merged}")
        return dp[n]
n = 8
#         0,1,2,3,4,5,6,7,8
ranges = [4,0,0,0,0,0,0,0,4]
t = Solution()
t.minTaps(n,ranges)

