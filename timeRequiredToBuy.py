class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        n=len(tickets)
        i=0
        count=0
        while tickets[k]!=0:
            if tickets[i%n]>0:
                tickets[i%n]=tickets[i%n]-1
                count+=1
            i+=1
        return count

        
