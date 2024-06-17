'''
LC637
Given the root of a binary tree, return the average val of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average val of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

'''

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
    

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        queue = [root]
        result = []
        while len(queue):
            currLength = len(queue)
            denominator = len(queue)
            currSum = 0
            while currLength:
                currRoot = queue.pop(0)
                currSum += currRoot.val
                if currRoot.left:
                    queue.append(currRoot.left)
                if currRoot.right:
                    queue.append(currRoot.right)
                currLength -= 1
            result.append(currSum / denominator)
        return result

def test1():
    obj = TreeNode(3)
    obj.left = TreeNode(9)
    obj.right = TreeNode(20)
    obj.right.left = TreeNode(15)
    obj.right.right = TreeNode(7)
    resObj = Solution()
    result = resObj.averageOfLevels(obj)
    return result

def test2():
    obj = TreeNode(1)
    obj.left = TreeNode(1)
    resObj = Solution()
    result = resObj.averageOfLevels(obj)
    return result

print(test2())


'''
LC111
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
'''

# Definition of TreeNode from prev problem

import math
class Solution2:
    def __init__(self):
        self.result = []

    def minDepth(self, root):
        def dfs(root, ht):
            if root:
                ht += 1
                if not root.left and not root.right:
                    self.result.append(ht)
                dfs(root.left, ht)
                dfs(root.right, ht)            
            return
        dfs(root, 0)
        return min(self.result) if self.result else 0
    
def test4():
    obj = TreeNode(3)
    obj.left = TreeNode(9)
    obj.right = TreeNode(20)
    obj.right.left = TreeNode(15)
    obj.right.right = TreeNode(7)
    resObj = Solution2()
    result = resObj.minDepth(obj)
    return result

def test5():
    obj = TreeNode(2)
    obj.right = TreeNode(3)
    obj.right.right = TreeNode(4)
    obj.right.right.right = TreeNode(5)
    obj.right.right.right.right = TreeNode(6)
    resObj = Solution2()
    result = resObj.minDepth(obj)
    return result

print(test4())
print(test5())