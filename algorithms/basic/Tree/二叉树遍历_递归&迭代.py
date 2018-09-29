'''
递归的遍历二叉树并打印
先序遍历：先打印根，在打印整颗左子树，再打印右子树

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class RecursiveSolution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


        if root == None:
            return []
        # print(root.val+" ")
        list = [root.val]

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        print (list + left + right)
        return list + left + right
    def inorderTraversal(self, root):
        '''
        
        :param root: 
        :return: 
        '''

    def