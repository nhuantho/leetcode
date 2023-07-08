object _9_Palindrome_Number {
  def isPalindrome(x: Int): Boolean = {
    var z = x
    if(z < 0) return false
    if(z < 10) return true
    if(z % 10 == 0) return false
    var y = z % 10
    z /= 10
    if(x < 100){
      if(y == z) return true
      else return false
    }
    while (y < z) {
      var a = z % 10
      y = y * 10 + a
      if (z == y) return true
      z /= 10
      if (z == y) return true
    }
    false
  }
  def main(args: Array[String]): Unit = {
    var x = _9_Palindrome_Number.isPalindrome(500)
    print(x)
  }
}
