class Solution(object):
    def binary(self, arr, x):
        left=0
        right=len(arr)-1
        while right>=left:
            mid=(left+right)//2
            if arr[mid]==x:
                return mid
            if arr[mid]>x:
                right=mid-1
            else:
                left=mid+1
        return left
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left=0
        right=len(arr)-1
        while (right-left+1)>k:
            if abs(arr[left]-x)>abs(arr[right]-x):
                left+=1
            else:
                right-=1
        return arr[left: right+1]







        counts=Counter(arr)
        
        left=self.binary(arr, x)
        if counts[arr[left]]>1:
            left=arr.index(arr[left])
        print(left)
        left_window=arr[left:min(left+k, len(arr))]
        right_window=arr[max(left-k, 0):left]
        print(left_window, right_window)
        if len(left_window)<k and len(right_window)<k:
            right_window=arr[:k]
            left_window=arr[k:]
        sum_left=float('inf')
        sum_right=float('inf')
        if len(left_window)==k:
            sum_left=0
            for j in left_window:
                
                sum_left+=abs(x-j)
                print(j,sum_left)
        if len(right_window)==k:
            sum_right=0
            for u in  right_window:
                sum_right+=abs(x-u)
        #print(sum_left, sum_right)
        
            
        if sum_right>sum_left:
            return left_window
        else:
            return right_window
        
