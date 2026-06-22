from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Store the numbers and count them

        frequent = Counter(nums)

        # List down the numbers with most common method 

        return [item[0] for item in frequent.most_common(k)]