class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum == target:
                        newElement = [nums[i], nums[j], nums[left], nums[right]]
                        if newElement not in result:
                            result.append(newElement)
                        left += 1
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        right -= 1

        return result
