class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num in range(len(nums1)):
            if len(nums2) == 0: break
            if nums1[num] == 0:
                nums1[num] = nums2.pop(0)
        nums1.sort()