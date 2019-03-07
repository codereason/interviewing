class Solution:
    def tree_depth(self,root):
        if root is None:return 0

        else:
            return 1+self.tree_depth(root.left) if self.tree_depth(root.left) > self.tree_depth(root.right) else self.tree_depth(root.right)+1