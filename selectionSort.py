class Solution: 
    def selectionSort(self, arr):
        #code here
        for b in range(len(arr)):
            min_index=b
            for j in range(b,len(arr)):
                if arr[min_index]>arr[j]:
                    min_index=j
                   # print(arr)
            arr[b], arr[min_index]= arr[min_index],arr[b] 
        return arr
