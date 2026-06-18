from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        first = 0
        last = n

        while last > first:
            mid = (first + last) // 2
            if nums[mid] < 0:
                first = mid + 1
            else:
                last = mid
        neg = first

        first = 0
        last = n

        while last > first:
            mid = (first + last) // 2
            if nums[mid] <= 0:
                first = mid + 1
            else:
                last = mid
        pos = n - first

        return max(pos, neg)