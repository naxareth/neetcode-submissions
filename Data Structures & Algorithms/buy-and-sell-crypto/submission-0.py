class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Get and store the lowest prices 
        lowest = prices[0]
        # Initialize the starting point
        highest = 0

        # Loop each number in prices
        for num in prices:
            # Check if the current price is lower
            if num < lowest:
                # Update the lowest price
                lowest = num
                #  If the current price subtracted by the lowest number is higher than the recorded highest price
            if num - lowest > highest:
                # Update the profit
                highest = num - lowest
        return highest