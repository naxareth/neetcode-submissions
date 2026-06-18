class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

            storage = {}

            for i, n in enumerate(nums):
                complement_num = target - n
                if complement_num in storage:
                    return [storage[complement_num], i]
                storage[n] = i
                
                    #Brute force
                    #n = len(nums)

                    #for i in range(n):
                    #   for j in range (i + 1, n):
                    #      if nums[i] + nums[j] == target:
                    #         return [i, j]
                # return []
