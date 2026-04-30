# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root):
        while root.left:
            root=root.left
        return root
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root:
            #print(root.val)
            if root.val>key:
                root.left=self.deleteNode(root.left, key)
            elif root.val<key:
                root.right=self.deleteNode(root.right, key)
            else:
                #if it has no children
                if not root.right and not root.left:
                    #print(root)
                    return None
                #if it has one children
                elif root.left and not root.right:
                    return root.left
                elif  root.right and not root.left:
                    return root.right
                else:
                    mini=self.inorder(root.right)
                    root.val=mini.val
                    root.right=self.deleteNode(root.right, mini.val)
                    
        return root
        
