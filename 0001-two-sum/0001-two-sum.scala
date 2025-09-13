import scala.util.control.Breaks._

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
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
}