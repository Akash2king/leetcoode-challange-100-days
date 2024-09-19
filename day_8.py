class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m1 = m - 1
        n1 = n - 1 
        right = m + n - 1

        while n1 >= 0:
            if m1 >= 0 and nums1[m1] > nums2[n1]:
                nums1[right] = nums1[m1]
                m1 -= 1
            else:
                nums1[right] = nums2[n1]
                n1 -= 1

            right -= 1