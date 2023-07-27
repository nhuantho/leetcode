object _67_Add_Binary {
  def addBinary(a: String, b: String): String = {
    (BigInt(a, 2) + (BigInt(b, 2))).toString(2)
  }

  def main(args: Array[String]): Unit = {
    println(addBinary("1010", "1011"))
  }
}
