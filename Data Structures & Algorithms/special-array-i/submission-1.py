class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        for number in range(len(nums) - 1):
            if nums[number] % 2 == nums[number + 1] % 2:
               return False
        return True