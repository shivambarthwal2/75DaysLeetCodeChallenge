class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0  # position for next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1