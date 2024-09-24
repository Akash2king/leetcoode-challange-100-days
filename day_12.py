class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        b=prices[0]
        for i in prices[1:]:
            if i<b:
                b=i
            if b<i:
                if abs(i-b) > p :
                    p=abs(i-b)
        return p