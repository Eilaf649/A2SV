class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr=[]
        x=0
        if num>0:
            s=num
            while s>0:
                arr.append(s%10)
                s=s/10
            if num<10:
                arr.append(num)
            arr.sort()
            if 0 not in arr:
                for i in range(len(arr)):
                    x+=arr[i]*10**(len(arr)-i-1)
            elif 0 in arr:
                couns=Counter(arr)
                x+=arr[couns[0]]*(10**(len(arr)-1))
                for j in range(couns[0]+1, len(arr)):
                    x+=arr[j]*(10**(len(arr)-j-1))
                    print(arr[j]*(10**(len(arr)-j-1)))
            print(arr)
            print(num<0)
        elif num<0:
            s=-num
            while s>0:
                arr.append(s%10)
                s=s/10
            if -num<10:
                arr.append(num)
            arr.sort(reverse=True)
            for k in range(len(arr)):
                    x+=arr[k]*(10**(len(arr)-k-1))
                    print(arr[k]*(10**(len(arr)-k-1)))
            x=-x
        return x




        

        
