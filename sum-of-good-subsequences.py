class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        count = Counter()
        res = Counter()

        mod = 10 ** 9 + 7

        for i in nums:
            count[i] += count[i - 1] + count[i + 1] + 1
            count[i] %= mod
            '''
            Why Do We Add res[a - 1] and res[a + 1]?
            Extending Existing Subsequences:
            When we append a to a subsequence ending with a - 1 or a + 1, we create new subsequences ending with a.
            The total sum of these new subsequences includes:
            The sum of the existing subsequences (res[a - 1] or res[a + 1]).
            Plus the value a for each subsequence extended (accounted for by a * count[...]).
            
            
            Why Do We Multiply a * (count[a - 1] + count[a + 1] + 1)?
            Adding a to Each Extended Subsequence:
            For each subsequence we're extending, we need to add a to the total sum because a is appended to each one.
            The total number of subsequences we're extending is count[a - 1] + count[a + 1].
            Including the Subsequence [a] Itself:
            The term 1 in count[a - 1] + count[a + 1] + 1 accounts for the new subsequence [a].
            We multiply a by this total count to get the sum contributed by a in all these subsequences.

            '''

            res[i] += res[i - 1] + res[i + 1] + i*(count[i - 1] + count[i + 1] + 1)
            res[i] %= mod
        
        return sum(res.values()) % mod
