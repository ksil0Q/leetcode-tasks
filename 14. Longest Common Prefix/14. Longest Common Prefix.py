class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                prefix += c
            else:
                break
        return prefix
