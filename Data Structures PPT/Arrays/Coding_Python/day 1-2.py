class GetMaxProfit:
    def maxProfit(self,prices:list,n:int) -> int:
        max_profit=0
        min_value = float('inf')
        for i in range(0,n):
            if min_value > prices[i]:
                min_value = prices[i]
            elif prices[i]-min_value > max_profit:
                max_profit = prices[i]-min_value
        return max_profit


prices = list(map(int,input().split()))
n=len(prices)
obj = GetMaxProfit()
print(f"Max profit is {obj.maxProfit(prices,n)}")