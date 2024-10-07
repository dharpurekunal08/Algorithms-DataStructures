# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        # Handle edge cases
        if s == '':
            return True
        if S > T:
            return False
        
        # Initialize pointer for s
        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:
                    return True
                j += 1
        
        return False
        # TC: O(n)
        # SC: O(1)