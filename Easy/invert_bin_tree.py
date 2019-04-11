### This Q was asked by Google to Max Howell (who created homebrew). Unfortunately, he couldn't answer.

def helper(root):
    if root==None:
        return
    temp=root.left
    root.left=root.right
    root.right=temp
    helper(root.left)
    helper(root.right)
    return

class Solution(object):
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        helper(root)
        return root