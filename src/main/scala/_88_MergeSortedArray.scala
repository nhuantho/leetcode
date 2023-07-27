object _88_MergeSortedArray {
  def merge(nums1: Array[Int], m: Int, nums2: Array[Int], n: Int): Unit = if (n > 0){
    if(m > 0 && nums1(m - 1) >= nums2(n - 1)){
      nums1(m + n - 1) = nums1(m - 1)
      merge(nums1, m - 1, nums2, n)
    }else{
      nums1(m + n - 1) = nums2(n - 1)
      merge(nums1, m, nums2, n - 1)
    }
  }
  def main(args: Array[String]): Unit = {
    var nums1 = Array(1,2,3,0,0,0)
    var nums2 = Array(2,5,6)
    var m = 3
    var n = 3
    merge(nums1, m, nums2, n)
    for(x <- nums1) println(x)
  }
}
