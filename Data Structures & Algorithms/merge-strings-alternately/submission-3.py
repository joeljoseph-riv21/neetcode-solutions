class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0 # two pointers are declared
        output = []
        while i < len(word1) and j < len(word2): # based on each iter. the index is changed and appended
            output.append(word1[i])
            i += 1 # increment to the next position
            output.append(word2[j])
            j += 1

        output.append(word1[i:]) # append everything left from both the strings
        output.append(word2[j:])
        return "".join(output)