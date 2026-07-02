from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TAKEAWAYS:
        One-Pass Hash Map:-
        - the current number is store in the trace dictionary as the key.
        - check if the complement (target - element) exists in the dictionary. 
        - so, dictionary is with element as its keys and index as values.
        """
      
        trace = {}
        for index, element in enumerate(nums):
            complement = target - element

            if complement in trace:
               return [trace[complement], index]
            trace[element] = index
        return []
