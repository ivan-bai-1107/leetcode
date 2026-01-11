from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_index = 0  # 指向最后一个唯一元素的位置
        
        for current_index in range(1, len(nums)):
            if nums[current_index] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[current_index]
        
        return unique_index + 1
