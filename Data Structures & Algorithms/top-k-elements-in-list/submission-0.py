from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]
       
        for keys, values in lookup.items():
            bucket[values].append(keys)

        output = []
        for i in range(len(bucket) - 1, 0, -1): 
            for num in bucket[i]:
                output.append(num)
               
                if len(output) == k:
                    return output
        

        

        