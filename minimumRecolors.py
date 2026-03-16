class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        ws=0
        bs=0
        left=0
        mini=float('inf')
        for right in range(len(blocks)):
            if blocks[right]=='W':
                ws+=1
            else:
                bs+=1
            #print(blocks[left: right+1], ws, bs, left, right)
            while right-left+1>k:
                #print(blocks[left:right+1], ws, bs, left, right)
                if blocks[left]=='W':
                    ws-=1
                else:
                    bs-=1
                left+=1
            if right-left+1==k:
                print(blocks[left: right+1], ws, bs, left, right)
                mini=min(mini, k-bs)
        return mini
