object _28_Find_the_Index_of_the_First_Occurrence_in_a_String {
  def strStr(haystack: String, needle: String): Int = {
    haystack.indexOf(needle)
  }

  def main(args: Array[String]): Unit = {
    println(strStr("sadbutsad", "sadbutsad"))
  }
}
