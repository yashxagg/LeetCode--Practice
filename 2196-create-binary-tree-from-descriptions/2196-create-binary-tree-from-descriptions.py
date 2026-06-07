# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        parents = set()
        
        for parent_val, child_val, is_left in descriptions:
            # 1. Ensure the parent node exists
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            # 2. Ensure the child node exists
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # 3. Establish the tree link
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # 4. Record tracking information
            children.add(child_val)
            parents.add(parent_val)
            
        # 5. The root is the only parent node that is never anyone's child
        for p in parents:
            if p not in children:
                return nodes[p]
                
        return None