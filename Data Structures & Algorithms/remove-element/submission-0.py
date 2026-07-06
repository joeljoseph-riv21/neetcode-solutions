class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        TAKEAWAYS:
        In Place Removal:-
        - checks if each value not equals target value.
        - if true, the number is copied and written over index value.

        Example logic:- 
        nums = [3,2,2,3], val = 3.

        loop run 1 (index = 0):
        - index 0: nums[0] is 3.
        - 3 != 3 is False.
        - Array state: [3, 2, 2, 3] (No change, k = 0)

        loop run 2 (index = 1): 
        - nums[1] is 2.
        - does 2 != val (2 != 3)? True. 
        - becomes nums[0] = nums[1].
        - result: The number 2 is copied and written over index 0, gives in-place move.
        - then k increments, so k becomes 1. Moving to next index. 
        - array state now: [2, 2, _, _] 
        """
        k = 0 # tracking counter (gatekeeper)

        for index in range(len(nums)): # the current pointer
            if nums[index] != val:
               nums[k] = nums[index]
               k += 1       
        return k