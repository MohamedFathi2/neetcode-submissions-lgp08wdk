class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        counter = 0
        for i in range(len(ans)):
            if counter == len(nums):
                counter = 0
            ans[i] = nums[counter]
            counter += 1
        return ans