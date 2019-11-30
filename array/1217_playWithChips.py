class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odds = 0
        evens = 0

        for chip in chips:
            if chip % 2 != 0:
                odds += 1

            else:
                evens += 1

        return min(evens, odds)
