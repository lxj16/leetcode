# 1313. Decompress Run-Length Encoded List
# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are a elements with value b in the decompressed list.

# Return the decompressed list.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]

# Constraints:

# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res += ([nums[i+1]] * nums[i])

        return res
