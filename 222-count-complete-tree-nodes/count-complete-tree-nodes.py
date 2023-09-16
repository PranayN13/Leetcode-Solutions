# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        l,r = root,root 
        height_Left, height_Right = 0, 0

        while l:
            height_Left +=1
            l = l.left
        
        while r:
            height_Right +=1
            r = r.right

        if height_Left == height_Right:
            return pow(2,height_Left) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        