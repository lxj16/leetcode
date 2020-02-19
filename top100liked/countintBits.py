# 338. Counting Bits

# Add to List

# Share
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]*(num+1)
        offset = 1
        for i in range(1, num+1):
            if offset*2 == i:
                offset *= 2
            result[i] = result[i-offset] + 1
        return result
        
class Solution2:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i // 2])
        return dp