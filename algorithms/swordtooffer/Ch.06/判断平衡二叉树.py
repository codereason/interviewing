class Solution:
    def isBST(self,root):
        if root is None:
            depth=0
            return True
        if self.isBST(root.left) and self.isBST(root.right):
            LeftDepth = self.getLength(root.left)
            RightDepth = self.getLength(root.right)
            if -1<= LeftDepth - RightDepth <= 1:
                return True
        return False

    def getLength(self,root):
        if root is None:return 0
        return max(self.getLength(root.left),self.getLength(root.right))+1