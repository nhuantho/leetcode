
/**

Definition for singly-linked list.
class ListNode(_x: Int = 0, _next: ListNode = null) {
var next: ListNode = _next
var x: Int = _x
}
 */

object _21_Merge_Two_Sorted_Lists {
  def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
    if (list1 == null) list2
    else if (list2 == null) list1
    else if (list1.x <= list2.x) {
      new ListNode(list1.x, mergeTwoLists(list1.next, list2))
    }else{
      new ListNode(list2.x, mergeTwoLists(list1, list2.next))
    }
  }
  def main(args: Array[String]): Unit = {
    var a = new ListNode(1)
    a.next = new ListNode(2)
    a.next.next = new ListNode(4)
    var b = new ListNode(1)
    b.next = new ListNode(3)
    b.next.next = new ListNode(4)
    var m = mergeTwoLists(a, b)
    while (m.next != null){
      println(m.x)
      m = m.next
    }
  }
}
