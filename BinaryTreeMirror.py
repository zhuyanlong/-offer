class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Mirror(self , pRoot ):
        if pRoot==None:
            return
        pRoot.left,pRoot.right=pRoot.right,pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)

def Travel(root):
    if root==None:
        return
    Travel(root.left)
    print(root.val)
    
    Travel(root.right)

def main():
    t=TreeNode(8)
    t.left=TreeNode(6)
    t.right=TreeNode(10)
    t.left.left=TreeNode(5)
    t.left.right=TreeNode(7)
    t.right.left=TreeNode(9)
    t.right.right=TreeNode(11)
    s=Solution()
    s.Mirror(t)
    Travel(t)

main()