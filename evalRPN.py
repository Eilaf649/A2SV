class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        flag=True
        stack=[]
        ordo={'+':0, '-':0, '*':1, '/':1}
        nums=[]
        if len(tokens)==1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] in ordo.keys():
                #first operation
                #print(nums)
                if flag and len(nums)>=2:
                    x=int(nums.pop())
                    y=int(nums.pop())
                    #print(x,y, tokens[i])
                    if tokens[i]=='*':
                       prod=x*y
                    elif tokens[i]=='/':
                        if abs(float(y)/float(x))<1:
                            prod=0
                        else:
                            # to round numbers correctly
                            if y%x!=0 and float(y)/float(x)<1:
                                prod=(y//x)+1
                            else:
                                prod=(y)//(x)
                    elif tokens[i]=='+':
                        prod=x+y
                    elif tokens[i]=='-':
                        prod=y-x
                    nums.append(prod)
                    
                    #print(nums)
            else:
                nums.append(tokens[i])

        return nums[-1] 
                
        
