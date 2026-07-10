class Solution:
    """
    TAKEAWAYS:
    - a hash set is created.
    - for each number, it performs a clever check: if the number immediately preceding it (num - 1) is not in the set,
    then num must be the start of a new potential consecutive sequence.
    - if num - 1 is in the set, we skip num because we would have already handled this sequence starting from num - 1.

    Inner loop:-
    - once we get the true consecutive, it increments current streak and current number.
    - the process continues until all potential starting numbers have been checked, and finally, the longest is returned.
    """
    def longestConsecutive(self, nums: List[int]) -> int: 
        if not nums:
            return 0

        trace = set(nums) 
        longest = 0 # for getting the longest streak seen so far.

        for num in trace:
            if num-1 not in trace: # the approach is effective because while loop runs only when the number is not present, others will be there inplace.
                current_number = num  
                current_streak = 1 

                while current_number + 1 in trace: # counting number begins.
                      current_number = current_number + 1
                      current_streak += 1

                longest = max(longest, current_streak) # gets the longest consecutive 
        return longest