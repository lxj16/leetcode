class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev_point = points[0]
        time = 0

        for cur_point in points[1:]:
            time += max(abs(prev_point[0] - cur_point[0]),
                        abs(prev_point[1] - cur_point[1]))
            prev_point = cur_point

        return time
