object _104_MaximumDepthofBinaryTree {
  def maxDepth(root: TreeNode): Int = {
    if(root == null) 0
    else{
      var lDepth = maxDepth(root.left)
      var rDepth = maxDepth(root.right)
      if(lDepth > rDepth) lDepth + 1
      else rDepth + 1
    }
  }

  def main(args: Array[String]): Unit = {
    var root = new TreeNode(1)
    root.left = new TreeNode(2)
    root.right = new TreeNode(2)
    root.left.left = null
    root.left.right = new TreeNode(3)
    root.right.left = null
    root.right.right = new TreeNode(3)
    var res = maxDepth(root)
    println(res)
  }
}
