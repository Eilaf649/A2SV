class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        shared=set(list1)&set(list2)
        shared=list(shared)
        list1=list(list1)
        list2=(list2)
        min=10000
        res={}
        r=[]
        if len(shared)>1:
            for i in range(len(shared)):
                res[shared[i]]=list1.index(shared[i])+list2.index(shared[i])
                if res[shared[i]]<=min:
                    min=res[shared[i]]
                    ind=i
            for key, value in res.items():
                if value==min:
                    r.append(key)
            return (r)
        return(list(shared)) 
