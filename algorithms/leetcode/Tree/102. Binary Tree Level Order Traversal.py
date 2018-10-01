'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
应该使用队列的方法最好不过
'''
import collections


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        list = []

        Queue = collections.deque()
        Queue.append(root)
        while len(Queue) != 0:
            tmp = []
            length = len(Queue)
            for i in range(length):
                r = Queue.popleft()
                tmp.append(r.val)
                if r.left:
                    Queue.append(r.left)
                if r.right:
                    Queue.append(r.right)
                    # print(tmp)
            list.append(tmp)

        return list
