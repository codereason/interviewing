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
        print(list + left + right)
        return list + left + right

    def inorderTraversal(self, root):
        '''
        
        :param root: 
        :return: 
        '''
        if root == None:
            return []
        list = [root.val]

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        # print (list + left + right)
        return left + list + right

    def postorderTraversal(self, root):
        if root == None:
            return []
        list = [root.val]

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        print(list + left + right)
        return left + right + list


'''
用非递归方法的二叉树遍历
'''


class IterativeSolution():
    def preorderTraversal(self, root):
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
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
            return list

    def inorderTraversal(self, root):
        stack = []
        list = []
        if root == None:
            return []
        else:

            while stack or root:#考察当前节点
                if root:
                    stack.append(root)
                    root = root.left
                    # 把当前节点为根，其树的左边界都往栈压

                else:
                    root = stack.pop()  ##考察那个左孩子是空的栈顶，并考察他的右孩子，如果右孩子是空，往上回溯
                    list.append(root.val)
                    root = root.right

            return list

    def postorderTraversal(self, root): #左右中
        '''
        后续是左右中，可以逆转为中右左，
        而前序是中左右，只要吧前序的稍改一下再逆序打印即可
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