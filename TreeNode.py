# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rec(self, root):
        res=[]
        if root:
            self.res.append(root.val)
            self.rec(root.left)
            self.rec(root.right)

        
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.res=[]
        self.rec(root)
        return self.res


        
