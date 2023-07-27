object _70_Climbing_Stairs {
  def climbStairs(n: Int): Int = {
    if(n > 2) climbStairs(n - 1) + climbStairs(n - 2)
    else n
  }

  def main(args: Array[String]): Unit = {
    println(climbStairs(3))
  }
}
