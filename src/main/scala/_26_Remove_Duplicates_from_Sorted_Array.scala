import scala.collection.immutable.Set

object _26_Remove_Duplicates_from_Sorted_Array {
  def removeDuplicates(nums: Array[Int]): Int = {
    var count = 0
    var index = 0
    for(i <- 1 to nums.length - 1){
      if(nums(i - 1 ) == nums(i)){
        count += 1
      }else{
        index += 1
        nums(index) = nums(i)
      }
    }
    nums.length - count
  }

  def main(args: Array[String]): Unit = {
    print(removeDuplicates(Array(0,0,1,1,1,2,2,3,3,4)))
  }
}
