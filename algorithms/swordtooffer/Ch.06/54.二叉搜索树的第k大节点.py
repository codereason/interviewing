class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        # print(root.val+" ")
        list = [root.val]

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        print (list + left + right)
        return  left +list   + right

    def KthNode(self,root,k):
        return self.inorderTraversal(root)[:k]


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution2:
    # 返回对应节点TreeNode，注意是节点不是节点的值
    def KthNode(self, root, k):
        # write code here
        if k <= 0: return None
        list = self.inorderTraversal(root)
        return list[k - 1] if k - 1 < len(list) else None

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        # print(root.val+" ")
        list = [root]

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + list + right