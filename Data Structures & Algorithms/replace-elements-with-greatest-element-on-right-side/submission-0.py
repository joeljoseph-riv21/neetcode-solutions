class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        TAKEAWAYS:
        - Reverse Traversal:-
        - right pointer acts as a placeholder for the maximum value seen so far to the most right. 
        - later we compare the right pointer value with original value, retaining the maximum for right.
        - ultimately sorting in descending order. 
        """
        if not arr:
           return []

        right = -1 # init. right pointer to replace -1 at last to the max value.
        for i in range(len(arr) - 1, -1, -1):
            original_value = arr[i] # original value to update right pointer for the next iteration.
            arr[i] = right
            right = max(right, original_value) # used for next iteration.
        return arr



        