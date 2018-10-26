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
应该使用队列的方法最好不过，
还有其他思路暂时不想了
我们需要借助一个队列，由于队列是先进先出的，所以可以先让根入队，在根出队的同时打印根，并让根的左孩子入队，再让右孩子入队，这样一来，左孩子结点就存储在队头的位置，可以首先被访问；
被访问之后，左孩子出队的同时打印左孩子，并让左孩子的孩子入队；此时队列的下一个元素就是右孩子，右孩子出队的同时打印右孩子，并让右孩子的孩子入队；
以此类推，直到队列为空。

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
