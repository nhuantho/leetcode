object _13_Roman_to_Integer {
  def romanToInt(s: String): Int = {
    var res = 0
    val roman = Map(
      "I" -> 1,
      "V" -> 5,
      "X" -> 10,
      "L" -> 50,
      "C" -> 100,
      "D" -> 500,
      "M" -> 1000
    )
    var len = s.length - 1
    for(i <- 0 to len - 1){
      if(
        (s(i).toString == "I" && (s(i + 1).toString == "V" || s(i + 1).toString == "X")) ||
          (s(i).toString == "X" && (s(i + 1).toString == "L" || s(i + 1).toString == "C")) ||
          (s(i).toString == "C" && (s(i + 1).toString == "D" || s(i + 1).toString == "M"))
      ){
        res = res - roman(s(i).toString)
      }else{
        res = res + roman(s(i).toString)
      }
    }
    res = res + roman(s(len).toString)
    res
  }
  def main(args: Array[String]): Unit = {
    var x = romanToInt("MCMXCI")
    println(x)
  }
}
