class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        res=[]
        z=set(numbers)
        for i in range(len(numbers)):
            if target-numbers[i] in z and numbers.index(target-numbers[i])!=i:
                res.append(i+1)
                res.append(numbers.index(target-numbers[i])+1)
                break
            else:
                i+=1
        res.sort()
        return res

        
