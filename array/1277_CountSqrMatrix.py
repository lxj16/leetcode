class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # if A[i][j] == 0 then no matrix
        # dp[i+1][j+1] is the number of squares at matrix[i][j]
        Row, Col = len(matrix), len(matrix[0])
        dp = [[0] * (Col+1) for _ in range(Row+1)]
        ans = 0
        for i in range(Row):
            for j in range(Col):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
                    ans += dp[i+1][j+1]
        return ans
