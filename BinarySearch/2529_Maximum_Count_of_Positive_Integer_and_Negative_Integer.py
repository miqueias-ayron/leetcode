import math
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        first = 0
        last = n

        while last > first:
            mid = math.floor((first + last) / 2)
            if nums[mid] < 0:
                first = mid + 1
            else:
                last = mid
        neg = first

        first_ = 0
        last_ = n

        while last_ > first_:
            mid_ = math.floor((first_ + last_) / 2)
            if nums[mid_] <= 0:
                first_ = mid_ + 1
            else:
                last_ = mid_
        pos = n - first_

        return max(pos, neg)