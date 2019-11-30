class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A.sort()
        even = [x for x in A if x % 2 == 0]
        odd = [x for x in A if x % 2 != 0]

        zipped = zip(even, odd)
        return [num for nums in zipped for num in nums]
