class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        TAKEAWAYS:
        Hash Map:-
        - it straightforwardly, tracks frequencies and then filters elements.
        - returning the final output using list comprehension.
        """
        tracing = {}
        n = len(nums)//3

        for element in nums:
            tracing[element] = tracing.get(element, 0) + 1 # getting the value associated with the element key in the tracing dictionary.
                                                           # assigns 1 by incrementing, if its the first time seeing the key 0 is returned then 1 is added.
        return [element for element, freq in tracing.items() if freq > n]


        