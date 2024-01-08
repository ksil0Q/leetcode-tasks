from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(root: Optional[TreeNode]) -> str:

    res = []
    def tree_traverse(root: Optional[TreeNode]):
        if root.left == root.right == None:
            return root.val
        
        res.append(str(root.val))

        res.append('(')
        if root.left:
            val = tree_traverse(root.left)
            if val is not None:
                res.append(str(val))
        res.append(')')

        if root.right:
            res.append('(')
            val = tree_traverse(root.right)
            if val is not None:
                res.append(str(val))
            res.append(')')

    if not root:
        return ""
    else:
        val = tree_traverse(root)
        if val is not None:
            return str(val)

    return "".join(res)
            



###################################################

if __name__ == '__main__':
    # treeNode4 = TreeNode(4)
    # treeNode3 = TreeNode(3)
    # treeNode2 = TreeNode(2, treeNode4)
    treeNode1 = TreeNode(1)

    print(tree2str(treeNode1))

    "0(0())(0()(0()()))"
    "0(0(0))(0()(0()(0)))"