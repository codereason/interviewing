'''
103. Binary Tree Zigzag Level Order Traversal
Medium

1417

81

Add to List

Share
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        q = []
        node = root
        q.append(node)
        flag = 1
        while q != []:
            q_len = len(q)
            tmp = []

            for i in range(q_len):
                t = q.pop(0)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                tmp.append(t.val)
            if flag == -1:
                # print("chufa")
                tmp = tmp[::-1]
            flag *= -1
            res.append(tmp)
        return res