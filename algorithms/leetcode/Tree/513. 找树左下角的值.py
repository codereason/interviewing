'''
513. 找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。

 

示例 1:



输入: root = [2,1,3]
输出: 1
示例 2:



输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
 

提示:

二叉树的节点个数的范围是 [1,104]
-231 <= Node.val <= 231 - 1 
通过次数61,112提交次数83,577
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        queue = [root]
        while len(queue)!=0:
            length = len(queue)
            res = None
            for i in range(length):
                node = queue.pop(0)
                if i == 0:
                    res = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res.val