class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr=[i for i in range(1,n+1)]
        print(arr)
        index=0
        while len(arr)>1:
            index=(index+k-1)%len(arr)
            print(index)
            arr.pop(index)
        return arr[0]
