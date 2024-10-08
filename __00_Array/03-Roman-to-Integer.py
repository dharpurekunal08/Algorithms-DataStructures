# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        sumn = 0
        n = len(s)
        i = 0
        while i < n:
            if i < n-1 and d[s[i]] < d[s[i+1]]:
                sumn += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                sumn += d[s[i]]
                i += 1
        return sumn