class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        counter = 0
        for i in range(len(nums) * 2):
            if counter == len(nums):
                counter = 0
            ans.append(nums[counter])
            counter += 1
        return ans