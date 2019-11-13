# coding=utf-8
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        双指针
             找出最高点
            分别从两边往最高点遍历：如果下一个数比当前数小，说明可以接到水
        """

        if len(height) <= 1:
            return 0

        max_height = 0
        max_height_index = 0

        # 找到最高点
        for i in range(len(height)):
            h = height[i]
            if h > max_height:
                max_height = h
                max_height_index = i

        area = 0

        # 从左边往最高点遍历
        tmp = height[0]
        for i in range(max_height_index):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])

        # 从右边往最高点遍历
        tmp = height[-1]
        for i in reversed(range(max_height_index + 1, len(height))):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])

        return area


print  Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
