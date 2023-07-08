import scala.collection.mutable.Stack

object _20_Valid_Parentheses {
  def isValid(s: String): Boolean = {
    if(s(0).toString == ")" || s(0).toString == "]" || s(0).toString == "}") return false
    var len = s.length - 1
    var st = Stack[String]()
    for(i <- 0 to len){
      var sindex = s(i).toString
      if(sindex == "[" || sindex == "(" || sindex == "{"){
        st.push(sindex)
      }else if(st.isEmpty == false) {
        var sttop = st.top.toString
        if ((sindex == ")" && sttop == "(") || (sindex == "]" && sttop == "[") || (sindex == "}" && sttop == "{")) st.pop()
        else st.push(sindex)
      }else st.push(sindex)
    }
    if(st.isEmpty) return true
    false
  }
  def main(args: Array[String]): Unit = {
    println(isValid("()[]{}"))
  }
}
