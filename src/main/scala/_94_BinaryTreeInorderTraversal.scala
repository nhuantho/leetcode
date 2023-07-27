object _94_BinaryTreeInorderTraversal {
  def inorderTraversal(root: TreeNode): List[Int] = {
    if(root == null) List()
    else inorderTraversal(root.left) ++ List(root.value) ++ inorderTraversal(root.right)
  }

  def main(args: Array[String]): Unit = {
    var root = new TreeNode(1)
    root.left = null
    root.right = new TreeNode(2)
    root.right.left = new TreeNode(3)
    root.right.right = null
    var l = inorderTraversal(root)
    for(i <- l) println(i)
  }
}
