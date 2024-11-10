class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        lookup = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap = []
        ans = ''
        for i in lookup:
            if i[0]!=0:
                heapq.heappush(heap, i)
        
        while heap:
            count, char = heapq.heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                if not heap:
                    return ans
                count2, char2 = heapq.heappop(heap)
                ans += char2
                count2 += 1
                if count2 != 0:
                    heapq.heappush(heap, (count2, char2))
            else:
                ans+= char
                count += 1
            if count:
                heapq.heappush(heap, (count, char))
        return ans
