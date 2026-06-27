class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        prefix = 1
        for forward in range(len(nums)):
            output[forward] = prefix
            prefix = prefix * nums[forward]

        suffix = 1
        for backward in range(len(nums) - 1, -1, -1):
            output[backward] = output[backward] * suffix
            suffix = suffix * nums[backward]
             
        return output