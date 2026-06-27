class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threesums = []

        for i, n in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                thesum = nums[i] + nums[left] + nums[right]
                if thesum  == 0:
                    threesums.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                if thesum < 0:
                    left += 1
                if thesum > 0:
                    right -= 1
        return threesums
