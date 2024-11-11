class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        travel = {}
        tickets.sort()
        for src, dst in tickets:
            travel.setdefault(src, []).append(dst)
        
        res = ["JFK"]
        n = len(tickets)

        def dfs(src):
            if len(res) == n + 1:
                return True
            
            if src not in travel:
                return False
            
            temp = travel[src]
            for i, v in enumerate(temp):
                travel[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                
                travel[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
        

        
