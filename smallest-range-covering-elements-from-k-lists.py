import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        k = len(nums)
        left = nums[0][0]
        right = nums[0][0]

        for i in range(k):
            curr = nums[i]
            left = min(left, curr[0])
            right = max(right, curr[0])
            heapq.heappush(pq, (curr[0], i, 0))
        
        track = (left, right)

        while True:
            val, idx, ptr = heapq.heappop(pq)
            ptr += 1

            if ptr == len(nums[idx]):
                break

            heapq.heappush(pq, (nums[idx][ptr], idx, ptr))

            left = pq[0][0]
            right = max(right, nums[idx][ptr])

            if track[1] - track[0] > right - left:
                track = (left, right)
        
        return list(track)



