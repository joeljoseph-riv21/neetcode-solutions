class Solution:
    """
    TAKEAWAYS:
    Merge Sort:-
    - divide and conquer.
    - recursive function call.
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums   # base case.

        middle = len(nums)//2
        left = self.sortArray(nums[:middle]) # 'self' is added to mention these function belong to class Solution.
        right = self.sortArray(nums[middle:]) # divide the array into 2 parts by midpoint.
        
        return self.merge(left, right) # conquer, merge the halves to one.

    def merge(self, left: List[int], right: List[int]) -> List[int]: 
        sorted_array = []
        i = j = 0  # tracking position with init. two pointers with 0.

        while i < len(left) and j < len(right): # compare number from both parts and make sorted_array.
              if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1

              else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:]) # in case if any numbers missing from either side, a valid append.
        return sorted_array