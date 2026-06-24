class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Initialize pointers
        left = 0
        right = len(numbers) - 1

        # Loop until both pointers meet in the middle
        while left < right:
            # Add two numbers
            theSum = numbers[left] + numbers[right]
            # Compare the sum to the target
            if theSum == target:
                return [left + 1, right + 1]
            if theSum < target:
                left += 1
            if theSum > target:
                right -= 1