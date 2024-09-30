class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 1
        for rp in range(1, len(nums)):
            if nums[rp-1] != nums[rp]:
                nums[lp] = nums[rp]
                lp += 1
        return lp