'''
199. Binary Tree Right Side View
Medium

1384

74

Favorite

Share
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
Accepted
205.6K
Submissions
409.4K

就是level order travesal   也可以i用dfs做
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        if not root:
            return []
        res = []

        queue.append(root)
        while len(queue) != 0:
            tmp_list = []
            length = len(queue)
            for i in range(length):
                tmp = queue.pop(0)
                tmp_list.append(tmp.val)

                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(tmp_list[-1])
        return res


class Solution2:
    def __init__(self):
        self.result = []

    def rightSideView(self, root: TreeNode) -> List[int]:
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, depth):
        if root == None:
            return
        if len(self.result) == depth:
            self.result.append(root.val)
        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)