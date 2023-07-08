object _14_Longest_Common_Prefix {
  def longestCommonPrefix(strs: Array[String]): String = {
    if (strs.length == 1) return strs(0)
    var str1 = strs(0)
    var len = strs.length - 1
    var index = 0
    var res = ""
    while(index < str1.length){
      for (i <- 1 to len) {
        var strx = strs(i)
        if (strx.length == 0 || index > strx.length - 1 || strx(index) != str1(index)) return res
      }
      res = res + str1(index).toString
      index += 1
    }
    res
  }
  def main(args: Array[String]): Unit = {
    println(longestCommonPrefix(Array("flower","flower","flower","flower")))
  }
}
