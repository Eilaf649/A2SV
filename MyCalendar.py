class MyCalendar(object):

    def __init__(self):
        self.arr=[]

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        right=len(self.arr)
        left=0
        while left<right:
            mid=(left+right)//2
            if self.arr[mid][1]>startTime:
                right=mid
            else:
                left=mid+1
        if len(self.arr)==0:
            self.arr.append([startTime, endTime])
            return True
        if (left>0 and self.arr[left-1][1]>startTime) or (left<len(self.arr) and self.arr[left][0]<endTime):
            return False
        else:
            self.arr.insert(left, [startTime, endTime])
            return True        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
