class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = [s[i] for i in range(len(s)-1, -1, -1)] # s[:], slice assignment selects the existing list and appends the new from the right in-place. 
