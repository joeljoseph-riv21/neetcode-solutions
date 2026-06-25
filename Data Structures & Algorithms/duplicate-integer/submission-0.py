class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
           return False
           
        tracker = {}

        for index, element in enumerate(nums):
            if element in tracker:
               return True 
            tracker[element] = True

        return False


        
        