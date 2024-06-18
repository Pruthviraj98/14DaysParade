'''
LC207
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegreeDict = defaultdict(list)
        outdegreeDict = defaultdict(list)

        for req in prerequisites:
            indegreeDict[req[0]].append(req[1])
            outdegreeDict[req[1]].append(req[0])
        
        zeroIndeg = []
        numIndeg = 0
        # find zero indegree courses
        for i in range(numCourses):
            if i not in indegreeDict:
                numIndeg += 1
                zeroIndeg.append(i)
        
        # DFS through zero indeg
        while zeroIndeg:
            currNode = zeroIndeg.pop()
            for neigh in outdegreeDict[currNode]:
                indegreeDict[neigh].remove(currNode)
                if not indegreeDict[neigh]:
                    zeroIndeg.append(neigh)
                    numIndeg += 1
                    del indegreeDict[neigh]
        
        if numIndeg == numCourses:
            return True
        return False
            
                

'''
LC112
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        totals = []
        def dfs(root, currSum):
            if not root:
                return
            currSum += root.val
            if not root.left and not root.right:
                totals.append(currSum)
            
            dfs(root.left, currSum)
            dfs(root.right, currSum)
    
        dfs(root, 0)
        if targetSum in totals:
            return True
        return False


def test1():
    obj = TreeNode(1)
    obj.left = TreeNode(2)
    obj.right = TreeNode(3)
    resObj = Solution()
    result = resObj.hasPathSum(obj, 5)
    return result

print(test1())

'''
LC 323
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
'''

n = 5
edges = [[0, 1], [1, 2], [3, 4]]

class Solution2:
    def connectedComponent(self, edges, n):
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set([])
        count = 0

        def dfs(root):
            if root in visited:
                return
            visited.add(root)
            for i in adj[root]:
                if i not in visited:
                    dfs(i)


        for j in range(n):
            if j not in visited:
                dfs(j)
                count += 1

        return count

def test2():
    obj = [[0, 1], [1, 2], [3, 4]]
    resObj = Solution2()
    result = resObj.connectedComponent(obj, 5)
    return result

def test3():
    obj = [[0, 1], [1, 2], [2, 3], [3, 4]]
    resObj = Solution2()
    result = resObj.connectedComponent(obj, 5)
    return result

print(test2())
print(test3())



'''
LC 494

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


'''


def findTargetSumWays(nums, target):
    dp = {}
    def dfs(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        
        if (i, total) in dp:
            return dp[(i, total)]
        
        dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
        return dp[(i, total)]

    return dfs(0, 0)

print(findTargetSumWays(nums = [1,1,1,1,1], target = 3))