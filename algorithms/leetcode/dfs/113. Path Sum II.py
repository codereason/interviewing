'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """


        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        # def dfs(self,root,sum):
        res1,res,res2 = [],[],[]
        tmp = []
        if root is None:
            return []

        if root.val == sum and root.left is None and root.right is None:
            tmp.append(root.val)
            res.append(tmp)
            return res
        
        sum -= root.val

        if root.left:
            # print([root.val]+self.pathSum(root.left, sum))
            
            res1=root.val+self.pathSum(root.left, sum)
            
       
        if root.right:
            res2=root.val+self.pathSum(root.right, sum)
        return [res1]+[res2]
    def dfs(self, root, sum):
        
        return lst