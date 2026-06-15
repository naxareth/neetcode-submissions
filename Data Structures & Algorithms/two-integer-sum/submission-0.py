class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range (i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7

    input = Solution()

    output = input.twoSum(nums, target)
    if output:
        print("f{output}")
    else:
        print ("N/A")