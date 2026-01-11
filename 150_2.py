from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        # 双指针遍历
        i, j, k = 0, 0, len(nums)
        while i < k:
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
