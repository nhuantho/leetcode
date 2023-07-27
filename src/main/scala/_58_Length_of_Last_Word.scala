object _58_Length_of_Last_Word {
  def lengthOfLastWord(s: String): Int = {
    val str = s.replaceAll("\\s+", " ").trim().split(" ")
    str(str.length - 1).length
  }

  def main(args: Array[String]): Unit = {
    lengthOfLastWord("   fly me   to   the moon  ")
  }
}
