# coding=utf-8
class Solution(object):
    """
    暴力法 旋转k次
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        length = len(nums)
        if k + 1 == length: return nums
        for i in range(0, k):
            preVal = nums[-1]
            for j in range(0,length):
                tmp = nums[j]
                nums[j] = preVal
                preVal = tmp
        return nums
    """
    数组切片 分片旋转
    1,2,3,4,5   k=2   分别取部分，在组合 4,5 | 1,2,3
    """
    def rotate1(self,nums,k):
        if nums:
            split = k % len(nums)
            nums[:]=nums[-split:]+nums[:-split]

nums = [1, 2, 3]
Solution().rotate(nums, 4)
Solution().rotate1(nums, 4)
print nums
