class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for element in arr:
            count[element] = count.get(element, 0) + 1                    

        lucky = -1
        for key, value in count.items():
            if key == value:
               lucky = max(key, lucky)
        return lucky