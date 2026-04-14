class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        indices = []
        while i < len(nums):
            toLook = target - nums[i]
            if toLook in nums and nums.index(toLook) != i:
                res = [i, nums.index(toLook)]
                res.sort()
                return res
            else:
                i += 1
        return indices