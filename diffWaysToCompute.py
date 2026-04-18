def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def compute(self, expression1, expression2,h):
            if h=="*":
                return  expression1*expression2
            elif h=="+":
                return  expression1+expression2
            elif h=="-":
                print(expression1-expression2)
                return expression1-expression2
        result=[]
        if len(expression)==0:
            return ""
        elif len(expression)==1:
            di=int(expression[0])
            return [di]
        elif len(expression)==2 and expression[0].isdigit():
            di=int(expression)
            return [di]
        for i in range(len(expression)):
            if not expression[i].isdigit():
                print(i, expression[i])
                left=self.diffWaysToCompute(expression[:i])
                right=self.diffWaysToCompute(expression[i+1:])
                print(left)
                #print(left, right)
                #print(left)
                for l in left:
                    for r in right:
                        print(expression[i])
                        result.append(self.compute(l,r, expression[i]))

        return result
