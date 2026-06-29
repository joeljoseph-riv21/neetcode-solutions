class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        TAKEAWAYS:
        - Dutch National Flag algorithm:-
        - the main logic is executed with the center pointer as current element.
        - left for 0& 1s and right for 1& 2s to the end.
        - init. left pointer to move the zeros we got from center.
        - where right is decremented to shrink the unsorted region from the right.
        It moves to the next position to its left, marking the new boundary of 
        elements that still need to be processed.
        """
        left = 0
        center = 0
        right = len(nums) - 1

        while center <= right:
              if nums[center] == 0:
                 nums[left], nums[center] = nums[center], nums[left]
                 left += 1
                 center += 1

              elif nums[center] == 1:
                   center += 1
 
              elif nums[center] == 2:
                   nums[right], nums[center] = nums[center], nums[right]
                   right -= 1
              
                   

