class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s=""
        i=0
        p=1
        if len(chars)==1:
            return 1
        while i<len(chars)-1:
            if chars[i]!=chars[i+1]:
                if p>1:
                    s+=chars[i]
                    s+=str(p)
                else:
                    s+=chars[i]
                p=1
            elif i==len(chars)-2:
                if chars[i]==chars[-1]:
                    p+=1
                    s+=chars[i]
                    s+=str(p)
                    p=1
            else:
                p+=1
            i+=1
        print(s)
        if chars[-1]!=chars[-2]:
            s+=chars[-1]
        for i in range(len(s)):
            print(i)
            chars[i]=s[i]
        return len(s)
