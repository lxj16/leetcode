class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowHigh = []
        result = 0
        for col in range(len(grid)):
            highest = 0
            for row in grid:
                if row[col] > highest:
                    highest = row[col]
            rowHigh.append(highest)
        colHigh = [max(row) for row in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += min(colHigh[j],rowHigh[i]) - grid[i][j]
                
        return result