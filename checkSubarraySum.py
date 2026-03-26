class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_seen={0:-1}
        mod=0
        for i in range(len(nums)):
            mod= (mod+nums[i])%k
            if mod in mod_seen:
                if i-mod_seen[mod]>1:
                    return True
            else:
                mod_seen[mod]=i
        return False






        """
        z=[]
        zero=0
        pref=[0]*len(nums)
        pref[0]=nums[0]
        Flag=False
        for i in range(len(nums)):
            pref[i]=pref[i-1]+nums[i]
            if Flag==False and pref [i]==pref[i-1]:
                Flag=True 
            if pref [i]==pref[i-1] and Flag==True:
                zero+=1
            elif pref [i]!=pref[i-1]:
                Flag==False
                zero=0
        #print(pref)
        for h in range(1, len(pref)):
            if pref[h]%k==0 or zero>1:
                print(pref[h])
                return True
    
        left=0
        for right in range(len(nums)):
            sumi=pref[right]
            while sumi%k!=0 and left<len(nums):
                sumi-=nums[left]
                pref[right]=sumi
                left+=1
            print(pref)
            if right-left>1:
                return True

        suf=[0]*len(nums)
        w=len(nums)-1
        suf[0]=nums[w]
        print(len(nums)-1, w)
        for j in range(1,len(nums)):
            y= len(nums)-j-1
            suf[j]=suf[j-1]+nums[y]
        for r in range(1, len(suf)):
            if suf[r]%k==0 or zero>1:
                print(suf[r])
                return True
        print(suf)
        return False
        """
                





        
