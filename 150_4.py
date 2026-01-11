from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # 使用索引来追踪写入位置
        # 只要当前元素与前两个已保留的元素不同时，就保留它
        write_index = 2
        
        for read_index in range(2, len(nums)):
            # 如果当前元素不同于前两个已保留的元素，则保留它
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1
                
        return write_index