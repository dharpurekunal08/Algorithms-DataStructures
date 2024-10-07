# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Get the length of the shorter and longer word
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        
        # Initialize result list
        result = []

        # Merge characters alternately
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        # Append the remaining part of the longer word
        if len1 > len2:
            result.extend(word1[min_len:])
        else:
            result.extend(word2[min_len:])
        
        # Convert list to string and return
        return ''.join(result)