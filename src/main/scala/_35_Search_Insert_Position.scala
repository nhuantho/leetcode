object _35_Search_Insert_Position {
  def searchInsert(nums: Array[Int], target: Int): Int = {
    var len = nums.length
    for(i <- 0 to len - 1){
      if(nums(i) >= target){
        return i
      }
    }
    len
  }

  def main(args: Array[String]): Unit = {
    println(searchInsert(Array(1,3,5,6), 7))
  }
}
