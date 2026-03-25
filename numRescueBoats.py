class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        #print(people)
        count=0
        left=0
        right=len(people)-1
        while right>=left:
            print(left, right)
            if people[left]+people[right]<=limit:
                right-=1
                left+=1
                count+=1
            else:
                right-=1
                count+=1
        return count

