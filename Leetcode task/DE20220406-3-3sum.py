class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    newElement = [nums[i], nums[left], nums[right]]
                    if newElement not in output:
                        output.append(newElement)
                    left += 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return output
