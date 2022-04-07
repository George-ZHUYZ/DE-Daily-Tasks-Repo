class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1:
        #
        # result = []
        #
        # for i in range(len(nums)):
        #
        #     if len(result) > 0:
        #         break
        #     else:
        #         for j in range(i+1, len(nums)):
        #             if nums[i] + nums[j] == target:
        #                 result = [i,j]
        #                 break
        #
        # return result

        # Solution 2:

        roundTime = 0

        while len(nums) > 1:
            reminder = target - nums.pop(0)

            try:
                rmdIndex = nums.index(reminder)
            except ValueError:
                roundTime += 1
                continue
            else:
                return [0 + roundTime, rmdIndex + 1 + roundTime]
