class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        closedtoopen ={')':'(', '}':'{',']': '['}
        for j in s:
            if j in closedtoopen:
                if stack and stack[-1]==closedtoopen[j]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(j)
        return stack==[]
        if len(stack)==0:
            return True
        else:
            return False
            
