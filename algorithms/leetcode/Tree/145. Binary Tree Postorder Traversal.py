'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):  # 左右中
        '''
        后序遍历是左右中，可以逆转为中右左，
        而前序是中左右，只要吧前序的逻辑稍改一下再逆序打印即可
        :param root: 
        :return: 
        '''
        stack = []
        list = []
        if root == None:
            return []
        else:

            stack.append(root)
            while (stack):
                root = stack.pop()
                list.append(root.val)
                print(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)

            return list[::-1]

    def postorderTraversal_(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        # print(root.val+" ")
        list = [root.val]

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        # print (list + left + right)
        return left + right + list

    def postorderTraversal3(self, root):  # 左右中
        '''
        后序遍历是左右中，可以逆转为中右左，
        而前序是中左右，只要吧前序的逻辑稍改一下再逆序打印即可
        :param root: 
        :return: 
        '''
        stack = []
        list = []
        if root == None:
            return []
        else:

            stack.append(root)
            while (stack):
                root = stack.pop()
                list.append(root.val)
                print(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)

            return list[::-1]