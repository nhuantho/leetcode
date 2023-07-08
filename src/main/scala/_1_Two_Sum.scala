import scala.math
import scala.util.control.Breaks._
import scala.io.StdIn.readInt

object _1_Two_Sum {
  def twoSum(nums: Array[Int], target: Int): Unit = {
    var l = nums.length - 1
    var arr:Array[Int] = new Array[Int](2);
    breakable{
      var i = 0;
      for (i <- 0 to l - 1) {
        var check = 1
        breakable{
          for (j <- i + 1 to l) {
            if(nums(i) + nums(j) == target){
              check = 0
              arr(0) = i
              arr(1) = j
              break
            }
          }
        }
        if(check == 0){
          break
        }
      }
    }
    arr
  }
  def main(args: Array[String]): Unit = {
    println(twoSum(Array(3, 4, 2), 6))
  }
}
