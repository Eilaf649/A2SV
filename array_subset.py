#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        from collections import Counter
        counter_a= Counter(a)
        counter_b=Counter(b)
        
        if len(b)<=10**5:
            for item, count in counter_b.items(): 
                if counter_a[item]<count:
                    return False
            return True
        
    
    
    
    
