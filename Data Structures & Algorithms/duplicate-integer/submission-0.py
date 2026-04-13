class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i in nums:
            if i in hashTable:
                hashTable[i] += 1
            else:
                hashTable[i] = 1
        for i in hashTable:
            if hashTable[i] > 1:
                return True
        return False
