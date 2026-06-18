from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        if target < nums[low]:
            return 0
        if target > nums[high-1]:
            return high

        while low < high:
            mid = ( low + high )//2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        return low