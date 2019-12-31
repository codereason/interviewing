'''
173. Binary Search Tree Iterator
Medium

1869

257

Add to List

Share
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        self.q = []
        self.stack = []

        #二叉树 to list
        if root is None:
            self.q = []
        else:
            while self.stack or root:  # 考察当前节点
                if root:
                    self.stack.append(root)
                    root = root.left
                    # 把当前节点为根，其树的左边界都往栈压

                else:
                    root = self.stack.pop()  ##考察那个左孩子是空的栈顶，并考察他的右孩子，如果右孩子是空，往上回溯
                    self.q.append(root.val)
                    root = root.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.q.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.q != []

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()