class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max=strs[0]
        for word in strs[1:]:
            while max!=word[0:len(max)]:
                max=max[:-1]
                if len(max)==0:
                    return""
        return max
