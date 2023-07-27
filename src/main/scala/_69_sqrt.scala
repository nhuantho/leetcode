object _69_sqrt {
  def mySqrt(x: Int): Int = {
    var low = 1L
    var high = x + 1L
    while(low < high){
      var mid = (low + high) / 2
      if(mid * mid > x) high = mid - 1
      else low = mid + 1
    }
    (low - 1).toInt
  }

  def main(args: Array[String]): Unit = {
    println(mySqrt(17))
  }
}
