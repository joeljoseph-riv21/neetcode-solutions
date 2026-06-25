from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        logs = {}

        for values in strs:
            sorted_key = "".join(sorted(values))

            if sorted_key not in logs:
               logs[sorted_key] = []

            logs[sorted_key].append(values)

        return list(logs.values())