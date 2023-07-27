object _83RemoveDuplicatesfromSortedListEasy {
  def deleteDuplicates(head: ListNode): ListNode = {
    if(head == null) head
    else if(head.next == null) new ListNode(head.x, deleteDuplicates(null))
    else if (head.x == head.next.x) {
      deleteDuplicates(head.next)
    } else{
      new ListNode(head.x, deleteDuplicates(head.next))
    }
  }

  def main(args: Array[String]): Unit = {
    var a = new ListNode(1)
    a.next = new ListNode(1)
    a.next.next = new ListNode(2)
    a.next.next.next = new ListNode(3)
    a.next.next.next.next = new ListNode(3)
    var m = deleteDuplicates(a)
    while (m.next != null) {
      println(m.x)
      m = m.next
    }
  }
}
