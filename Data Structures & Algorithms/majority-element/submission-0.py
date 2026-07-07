class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        trace = {}
        n = len(nums)//2

        for element in nums:
            trace[element] = trace.get(element, 0) + 1

        return [element for element, occurance in trace.items() if occurance > n][0]
            
        