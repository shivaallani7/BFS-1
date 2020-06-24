# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

//Time Complexity: O(n)
//Space Complexity: O(2power(h)) or O(n)
// Did it run on Leet Code: Yes
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 
        q = deque([root])
        res = []
        while q:
            
            levNodes = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()                
                levNodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levNodes)    
        return res
                
