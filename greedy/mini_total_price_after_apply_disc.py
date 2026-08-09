class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        l = []
        for i in range(len(prices)):
            try:
                val = (prices[i]*(100-discounts[i]))/100
            except:
                val = prices[i]
            l.append(val)
        return sum(l)