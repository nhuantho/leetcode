object _100_Same_Tree {
  def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
    if(p == null && q == null) true
    else if(p != null && q != null){
      if(p.value != q.value) false
      else isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }else false
  }
}
