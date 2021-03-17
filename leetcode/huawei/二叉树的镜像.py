class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return
        pRoot.left,pRoot.right = pRoot.right, pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot