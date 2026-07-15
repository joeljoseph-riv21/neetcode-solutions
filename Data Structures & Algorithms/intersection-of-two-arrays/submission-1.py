class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        trace = set(nums1)
        output = set()
        for element in nums2:
            if element in trace:
                output.add(element)
        return list(output)