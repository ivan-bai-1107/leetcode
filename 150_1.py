from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 使用三个指针：i指向nums1有效元素的最后，j指向nums2的最后，k指向nums1的最后
        i = m - 1  # nums1中有效元素的最后一个索引
        j = n - 1  # nums2中最后一个元素的索引
        k = m + n - 1  # nums1中要填充的位置

        # 从后往前比较并放置元素
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # 如果nums2还有剩余元素，将其复制到nums1
        # 注意：如果nums1有剩余而nums2已经处理完，无需移动，它们已经在正确位置
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
