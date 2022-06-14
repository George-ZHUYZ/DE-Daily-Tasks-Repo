class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # pos = [-1, -1]
        #
        # if len(nums) > 0 and target in nums:
        #     for i in range(len(nums)):
        #         if nums[i] == target:
        #             if pos[0] == -1:
        #                 pos = [i, i]
        #             else:
        #                 pos[1] = i

        # return pos

        # if target not in nums:
        #     return [-1, -1]
        #
        # start = bisect_left(nums, target)
        # end = bisect_right(nums, target) - 1
        #
        # return [start, end]

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == target and nums[right] == target:
                return [left, right]
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1

        return [-1, -1]
