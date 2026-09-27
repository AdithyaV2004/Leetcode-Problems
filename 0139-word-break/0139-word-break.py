class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        idx=0
        n=len(s)
        dp=[None]*(n+1)
        dp[n]=True
        def decision_tree(idx):
            if dp[idx] is not None:
                return dp[idx]
            for i in wordDict:
                l=len(i)                
                if i==s[idx:idx+l]:
                    if decision_tree(idx+l):
                        dp[idx] = True
                        return True
            dp[idx]=False
            return False
        return decision_tree(0)

