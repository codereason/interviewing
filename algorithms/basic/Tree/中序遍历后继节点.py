'''
Write an algorithm to find the 'next' node (eg. in-order successor) of a given node in a binary search tree where each node has a link to its parent.

---------------------

本文来自 lalor 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/lalor/article/details/7621239?utm_source=copy 
 分为三种情况：
        1.一个节点有右孩子，则在中序遍历中，该节点的后继是它的右子树的最左节点。
        2. 这个节点是它父亲的左孩子，则该节点的后继节点是它的父亲
        3. 这个节点是它父亲的右孩子，则需要一直向上搜索，直到它们n-1代祖先是它第n代祖先的左孩子，则它的后继就是第n个祖先。如果一直搜索到根节点，也没有找到n-1代祖先是它第n代祖先的左孩子，则该节点是整个树的中序遍历中的最后一个节点，即它没有后继(or NULL)。

---------------------

本文来自 lalor 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/lalor/article/details/7621239?utm_source=copy 
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def fingSuccessor(self, node):
        if node is None:
            return None

        else:
            if node.right:
                return self.getTreeMostLeft(node.right)
            else:
                parent = node.parent
                while(parent):
                    if node is parent.left:
                        return parent
                    if node is parent.right:
                        node = parent
                        parent = node.parent

        return parent




    def getTreeMostLeft(self, node):
        if node is None:
            return None

        else:
            while (node.left):
                node = node.left

        return node
