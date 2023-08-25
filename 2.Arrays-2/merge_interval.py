class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : (x[0],x[1]))
        res = [[intervals[0][0] , intervals[0][1]]]
        prev_end = intervals[0][1]
        for interval in intervals[1:] :
            cur_start,cur_end = interval

            if cur_start <= prev_end :
                start,end = res.pop()
                res.append([start,max(cur_end,prev_end)])
            else :
                res.append([cur_start,cur_end])

            prev_end = max(prev_end,cur_end)
        
        return res