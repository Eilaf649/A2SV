class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        x=len(arr)
        h=arr
        i=0
        for u in range(x):
            if u>x-i-1:
                break
            if arr[u]==0:
                if u==x-i-1:
                    arr[x-1]=0
                    x-=1
                    break
                i+=1
        last=x-i-1
        for y in range(last,-1,-1):
            if arr[y]==0:
                arr[y+i]=0
                i-=1
                arr[y+i]=0
            else:
                arr[y+i]=arr[y]


