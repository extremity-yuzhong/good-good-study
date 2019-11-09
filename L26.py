class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        length = len(nums)
        r = 1
        s = 0
        for i in range(1, length):
            if nums[i] != nums[s]:
                r += 1
                s += 1
                nums[s] = nums[i]
        return r


nums = [1, 1, 1, 1, 1, 2, 2, 3]
nums = [1, 1, 2]
nums = []
print Solution().removeDuplicates(nums)
print nums
