object _66_Plus_One {
  def plusOne(digits: Array[Int]): Array[Int] = {
    var index = digits.length - 1
    digits(index) = digits(index) + 1
    while(index >= 0 && digits(index) == 10){
      if(index == 0 && digits(index) == 10){
        digits(0) = 0
      }else{
        digits(index) = 0
        digits(index - 1) = digits(index - 1) + 1
      }
      index -= 1
    }
    if(digits(0) == 0){
      return (1 +: digits)
    }
    digits
  }

  def main(args: Array[String]): Unit = {
    var arr = plusOne(Array(9, 8, 9))
    for(i <- 0 to arr.length - 1){
      println(arr(i))
    }
  }
}
