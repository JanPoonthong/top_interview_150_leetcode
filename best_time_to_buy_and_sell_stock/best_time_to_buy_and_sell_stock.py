class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_min = float('inf')
        current_max = 0
        for i in range(len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            profit = prices[i] - current_min
            if profit > current_max:
                current_max = profit

        return current_max


solution = Solution() 
# print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([2,4,1]))
