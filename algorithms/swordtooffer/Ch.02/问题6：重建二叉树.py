class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

'''
递归方法
'''
class Solution:
    def recon(self, list1, list2):
        '''
        
        :param list1: 前序
        :param list2: 中序
        :return TreeNode 
        '''
        if len(list1) == 0: return None
        root = TreeNode(list1[0])
        root.left = self.recon(list1[1:1+list2.index(list1[0])], list2[:list2.index(list1[0])])
        root.right = self.recon(list1[1+list2.index(list1[0]):], list2[list2.index(list1[0])+1:])
        return root
