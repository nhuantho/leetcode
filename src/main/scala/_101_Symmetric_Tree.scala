object _101_Symmetric_Tree {
  def isSymmetric(root: TreeNode): Boolean = {
    if(root.left == null && root.right == null) true

    var r = reverseTree(root.right)
    compare(root.left, r)
  }

  private def reverseTree(r: TreeNode): TreeNode = {
    if(r == null) r
    else new TreeNode(r.value, reverseTree(r.right), reverseTree(r.left))
  }

  private def compare(l: TreeNode, r: TreeNode): Boolean = {
    if(l == null && r == null) true
    else if(l != null && r != null){
      if(l.value != r.value) return false
      else compare(l.left, r.left) && compare(l.right, r.right)
    }else false
  }

  def main(args: Array[String]): Unit = {
    var root = new TreeNode(1)
    root.left = new TreeNode(2)
    root.right = new TreeNode(2)
    root.left.left = null
    root.left.right = new TreeNode(3)
    root.right.left = null
    root.right.right = new TreeNode(3)
    var res = isSymmetric(root)
    println(res)
  }
}
