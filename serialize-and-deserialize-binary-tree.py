# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder_conversion(node):
            if not node:
                res.append('NULL')
                return 
            res.append(str(node.val))
            preorder_conversion(node.left)
            preorder_conversion(node.right)
        
        preorder_conversion(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        # print(values)
    

        def tree_form():
            if not values:
                return None
            
            val = values.pop(0) # pop the first element of the array
            if val == 'NULL':
                return None
            
            
            node = TreeNode(int(val))
            node.left = tree_form()
            node.right = tree_form()
            return node
        return tree_form()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
