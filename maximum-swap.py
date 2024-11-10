class Solution:
    def maximumSwap(self, num: int) -> int:

        num = list(str(num))

        max_val = -1
        max_idx = - 1
        swap_to = -1

        for i in range(len(num) - 1, -1, -1):
            # max_val = max(max_val, num[i])
            if max_val < int(num[i]):
                max_val = int(num[i])
                max_idx = i
            if int(num[i]) < max_val:
                swap_to = i
                swap_from = max_idx
        
        if swap_to != -1:
            num[swap_from], num[swap_to] = num[swap_to], num[swap_from]

        return int(''.join(num))


        # numlst = list(str(num))
        # n = len(numlst)

        # l , r = [], []
        # curr_min = int(numlst[0])
        # curr_max = int(numlst[-1])

        # for i in range(1, len(numlst)-1):
        #     l.append(curr_min)
        #     r.append(curr_max)
        #     curr_min = min(curr_min, int(numlst[i]))
        #     curr_max = max(curr_max, int(numlst[n - i - 1]))
        
        # diff = float(-'inf')
        # idx = -1

        # for i in range(n-1):
        #     if curr_max[i] - curr_min[i] > diff:
        #         diff = curr_max[i] - curr_min[i]
        #         idx = i
        
        # new = 






        
