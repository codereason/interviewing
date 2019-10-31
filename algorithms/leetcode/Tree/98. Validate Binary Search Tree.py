'''
Medium

2432

357

Favorite

Share
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Accepted
480,324
Submissions
1,820,575

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        tree_list = []
        if root is None:
            return True


        def in_order_travel(root):
            if not root:
                return

            in_order_travel(root.left)
            tree_list.append(root.val)
            in_order_travel(root.right)

        in_order_travel(root)
        # print(tree_list)
        if len(tree_list) == 0 or len(tree_list) == 1: return True
        for i in range(len(tree_list) - 1):
            if tree_list[i] >= tree_list[i + 1]:
                return False
        return True
