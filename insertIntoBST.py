# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recurr(self, root, val):
        if root:
            if val>root.val:
                if not root.right:
                    root.right=TreeNode(val)
                else:
                    return self.insertIntoBST(root.right, val)
            elif val<root.val:
                if not root.left:
                    root.left=TreeNode(val)
                else:
                    return self.insertIntoBST(root.left, val)
            
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        self.recurr(root, val)
        return root
