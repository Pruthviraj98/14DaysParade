'''
LC863

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        ## Convert the tree to a graph and then bfs till kth level from target node
        adjacencyList = defaultdict(list)
        ## convert to graph via bfs or dfs (all we need is nodes and chidren)
        
        queue = [root]
        while queue:
            currLen = len(queue)
            while currLen:
                currLen = currLen - 1
                currNode = queue.pop(0)
                if currNode.left:
                    adjacencyList[currNode].append(currNode.left)
                    adjacencyList[currNode.left].append(currNode)
                    queue.append(currNode.left)
                if currNode.right:
                    adjacencyList[currNode].append(currNode.right)
                    adjacencyList[currNode.right].append(currNode)
                    queue.append(currNode.right)
        

        ## BFS till kth level from the target Node
        level = 0
        visited = set([target]) # adding this as we start from the target node
        queue = [target]
        result = []
        while queue:
            currentLength = len(queue)
            while currentLength:
                currentLength -= 1
                currentNode = queue.pop(0)
                if level == k: #if level is k, append currentNode
                    result.append(currentNode.val)
                else: #else bfs
                    for edge in adjacencyList[currentNode]:
                        if edge not in visited:
                            queue.append(edge)
                            visited.add(edge)
            level += 1
        return result

def test1():
    obj = TreeNode(3)
    obj.left = TreeNode(5)
    obj.right = TreeNode(1)
    obj.right.left = TreeNode(0)
    obj.right.right = TreeNode(8)
    obj.left.right = TreeNode(2)
    obj.left.left = TreeNode(6)
    obj.left.right.left = TreeNode(7)
    obj.left.right.right = TreeNode(4)
    resObj = Solution()
    result = resObj.distanceK(obj, target=obj.left, k=2)
    return result

print(test1())


'''
LC 417

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

'''

class Solution2:
    def pacificAtlantic(self, heights):
        # dfs to find the elements that touch either pacific or atlandic
        # store them in the set
        # get intersection of the list and return answer
        
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, ocean, prevHeight):
            if (i, j) in ocean or i < 0 or j < 0 or i > len(heights) - 1 or j > len(heights[0]) - 1 or heights[i][j] < prevHeight:
                return
            ocean.add((i, j))
            dfs(i, j + 1, ocean, heights[i][j])
            dfs(i, j - 1, ocean, heights[i][j])
            dfs(i + 1, j, ocean, heights[i][j])
            dfs(i - 1, j, ocean, heights[i][j])
        

        #  I MAKE MISTAKES HERE DURING LOOPING THROUGH ECCENTRIC PARTS OF THE GRAPH
        for i in range(m):
            dfs(0, i, pacific, heights[0][i])
            dfs(n - 1, i, atlantic, heights[n - 1][i])

        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, m - 1, atlantic, heights[i][m - 1])

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atlantic and (i, j) in pacific:
                    result.append([i, j])
        return result

def test2():
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    resObj = Solution2()
    result = resObj.pacificAtlantic(heights)
    return result

print(test2())


'''
NOTE: I also completed  LC 200, LC 102, LC107. But, as they are basics, I revised them on LEETCODE directly.
'''