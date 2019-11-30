class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numCount = {}
        for num in nums:
            if num in numCount.keys():
                numCount[num] += 1
            else:
                numCount[num] = 1

        for key, value in numCount.items():
            if value == 1:
                return key
