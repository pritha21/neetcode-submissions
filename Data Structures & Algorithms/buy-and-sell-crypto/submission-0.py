class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff=0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if (prices[j]-prices[i]<0) or (prices[j]-prices[i]==0):
                    continue
                else:
                    diff=prices[j]-prices[i]
                    if diff>max_diff:
                        max_diff=diff
        return max_diff

        