# coding=utf-8
class Solution(object):
    """
    暴力解法
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chs = dict()
        for chr in s:
            if(chr in chs):
                chs[chr] += 1
            else:
                chs[chr] = 1
        for chr in t:
            if(chr in chs):
                if chs[chr] - 1 == 0:
                    del chs[chr]
                else:
                    chs[chr] = chs[chr] - 1
            else:
                chs[chr] = 1
        sum = 0
        for key in chs:
            sum += chs[key]

        if sum == 0:
            return True
        else:
            return False
    """
     先排序 后比较 
    """
    def isAnagram1(self, s, t):
        return True if  sorted(s) == sorted(t) else False

print Solution().isAnagram("aacc","ccac")
print Solution().isAnagram1("aacc","ccac")