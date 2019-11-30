class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []

        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.
