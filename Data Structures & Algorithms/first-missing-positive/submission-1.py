class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        TAKEAWAYS:
        Hash Set:-
        - the input list is put into a set.
        - iteration starts from integer 1 to len(nums)+1.
        - outputs the smallest positive integer found, all positive integers up-to 
        len(nums) are present, and len(nums) + 1 is the actual answer.
        """
        trace_set = set(nums)

        for element in range(1, len(nums) + 2):
            if element not in trace_set: # nums=[-2, -1, 0]: here, len(nums) is 3. 
                return element           # the loop will check i = 1, 2, 3, 4. Outputs 1 immediately and terminates, will never go& check the last.

            
        