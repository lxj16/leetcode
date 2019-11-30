class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        for stone in S:
            if stone in J:
                counter +=1
                
        return counter