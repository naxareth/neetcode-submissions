class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a list of numbers to store
        seen = {}

        # loop through each numbers

        for i, n in enumerate(nums):

            # if the number is in seen
            if n in seen:
                return True
            # else just keep inserting to storage
            seen[n] = i
        # No duplicated numbers
        return False