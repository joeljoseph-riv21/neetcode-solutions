class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        TAKEAWAYS:
        - the prefix sum logic, stores the prefix sum of the array up to the current element by accumulation.
        when nums = [2, -1, 1, 2]:
        after 1, prefix_sum is 2.
        after 2, prefix_sum is 2 + (-1) = 1.
        after 3, prefix_sum is 2 + (-1) + 1 = 2.
        """
        trace = {0:1} # init. a hash map in a way it handles a subarray itself (when getting 0 or prefix_sum == k).
        prefix_sum = 0
        count = 0

        for element in nums:
            prefix_sum += element

            if (prefix_sum - k) in trace:
                count += trace[prefix_sum - k]

            trace[prefix_sum] = trace.get(prefix_sum, 0) + 1
        
        return count


        