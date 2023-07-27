object _27_Remove_Element {
  def removeElement(nums: Array[Int], `val`: Int): Int = {
    val res = nums.filter(_ != `val`)
    var len = res.length
    for(i <- 0 to len - 1){
      nums(i) = res(i)
    }
    len
  }

  def main(args: Array[String]): Unit = {
    print(removeElement(Array(3,2,2,3), 3))
  }
}
