class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        minutes = sorted(time_to_minutes(i) for i in timePoints)

        min_diff = abs(1440 + minutes[0] - minutes[-1])
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        return min_diff
        
