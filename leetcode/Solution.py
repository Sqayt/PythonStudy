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

    def checkIfPangram(self, sentence):
        sentence = sentence.lower()
        lst = {}
        for i in range(97, 123):
            lst[i] = 0

        for el in sentence:
            d = ord(el)
            lst[d] += 1

        return 0 not in lst.values()

    def sortPeople(self, names, heights):
        tmp = {}

        for i in range(len(heights)):
            tmp[heights[i]] = names[i]

        result = sorted(tmp.items(), reverse=True)
        return [v for k, v in result]

    def separateDigits(self, nums):
        result = []
        for num in nums:
            result.append(self.convert(num))

        return result

    def convert(self, num):
        tmp = []
        while num > 1:
            tmp.append(num)
            num /= 10

        return tmp


if __name__ == '__main__':
    print(Solution().separateDigits([13, 25, 83, 77]))
