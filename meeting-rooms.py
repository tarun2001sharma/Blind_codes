class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        
        for i in range(1, len(intervals)):
            temp1 = intervals[i-1][1]
            temp2 = intervals[i][0]

            if temp1 >temp2:
                return False
        return True
        
