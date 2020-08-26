# Definition for a binary tree node.
#二叉查找树中，第k个最大的节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归形式
class Solution:
    def kthLargest(self, root, k):
        self.res=[]
        self.dfs(root,k)
        print(self.res)
        return self.res[-k]
    def dfs(self,root,k):
        if root==None:
            return
        self.dfs(root.left,k)
        self.res.append(root.val)
        self.dfs(root.right,k)

#栈的形式，道行不够，这道题还是没法做出来
# class Solution:
#     def kthLargest(self, root, k):
#         # print("Y")
#         if root==None:
#             return
#         stack=[root]
#         res=[]
#         while stack:
#             while stack[-1].right:
#                 stack.append(stack[-1].right)
#             # while stack:s
#             while stack:
#                 tmp=stack.pop()
#                 res.append(tmp.val)
#                 if tmp.left:
#                     stack.append(tmp.left)
#         print(res)
#         return 0

def main():
    t=TreeNode(5)
    t.left=TreeNode(3)
    t.right=TreeNode(6)
    t.left.left=TreeNode(2)
    t.left.right=TreeNode(4)
    t.left.left.left=TreeNode(1)
    t.left.left.right=TreeNode(2.5)
    s=Solution()
    k=3
    print(s.kthLargest(t,k))
    # s.kthLargest(t,k)

main()