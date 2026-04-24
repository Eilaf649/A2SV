class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        right=len(letters)-1
        left=0
        while left<right:
            mid=(left+right)//2
            print(left, right,mid, letters[left], letters[right], letters[mid], letters[right]<=target)
            if letters[mid]<=target:
                left=mid+1
            else:
                right=mid
                
        #print(left, right,mid, letters[left], letters[right], letters[mid])
        if letters[left]>target:
            return letters[left]
        else:
            return letters[0]
                
        
