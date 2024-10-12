class Solution:
    '''
    The most optmial solution will be a O(nlogn) time complexity and O(n)space complexity Linear scan through the meetings using two pointers.

    We define two pointers start_ptr and end_ptr. 
    The idea is to sort the start and end times of intervals in separate arrays.
    
    Then we will instantiate a while loop which keeps track of both the pointers

    If start time < end time that means we need a room for that conference meeting
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # start_times = sorted(intervals, key=lambda x: x[0])

        if not intervals:
            return 0

        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        ptr_start = 0
        ptr_end = 0

        max_rooms = 0
        curr_rooms = 0

        while ptr_start < len(intervals):
            if start_times[ptr_start] < end_times[ptr_end]:
                curr_rooms += 1
                ptr_start += 1
            else:
                curr_rooms -= 1
                ptr_end += 1

            max_rooms = max(max_rooms, curr_rooms)
        
        return max_rooms

        
        
