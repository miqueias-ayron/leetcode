import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1
        mid_index = 0

        while last_index >= first_index :
            mid_index = math.floor((first_index + last_index )/2)
            if target > nums[mid_index]:
                first_index = mid_index + 1
            elif target < nums[mid_index]:
                last_index = mid_index - 1
            else:
                return mid_index
        return -1