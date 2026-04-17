class Solution(object):
    def recurr(self, right, left):
        if s[right]=="]":
            for i in range(s[left]):
                ans+= s[left+1:right]
            return ans
        return self.recurr(s,right-1, left+2)
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        current_str=""
        current_num=""
        for i in s:
            if i!="]":
                stack.append(i)
            
            else:
                current_str=""
                while stack[-1]!="[":
                    current_str=stack.pop()+current_str
                stack.pop()
                current_num=""
                while stack and stack[-1].isdigit():
                    current_num=stack.pop()+current_num
                print(current_num)
                current_str= int(current_num)*current_str
                stack.append(current_str)
        return "".join(stack)
       






        """
        return self.recurr[s, 0, len(s)]
        """
            
            

        
