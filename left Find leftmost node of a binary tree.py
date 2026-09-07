class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def left_most(root):
  if root is None:
    return None

  if root.left == None:
    return root.val
  else:
    return left_most(root.left)

def left_most_iterative(root):
   
  if root is None:
    return None
   
    
  current = root
  while current.left is not None:
    current = current.left

  return current.val
