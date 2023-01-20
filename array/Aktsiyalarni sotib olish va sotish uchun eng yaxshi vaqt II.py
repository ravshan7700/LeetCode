class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minn=min(prices)
        index=prices.index(minn)
        maxx=prices[0]

        for i in range(index, len(prices)):
            if maxx < i:
                maxx=i
        index_maxx=prices.index(maxx)

        return maxx-minn