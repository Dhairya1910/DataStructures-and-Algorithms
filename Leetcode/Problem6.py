class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        indexes = {}
        offset = 0
        for i in range(len(s)):
            char = s[i]
            index = indexes.get(char)
            if index is not None and index >= offset:
                length = i - offset
                offset = index + 1
                if length > longest:
                    longest = length
            indexes[char] = i
        return max(longest, (len(s) - offset))