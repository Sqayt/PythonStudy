from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        stack, ret_val = list(), deque()
        stack.append(root)

        while stack:
            node = stack.pop()

            ret_val.appendleft(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return ret_val


