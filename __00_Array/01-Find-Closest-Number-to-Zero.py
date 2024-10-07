# 2239. Find Closest Number to Zero


class Solution:
    def findClosestNumber(self, nums) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
            
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        TC: O(n)
        SC: O(1)

    def findClosestNumber2(self, nums) -> int:
        nums.sort(key=lambda x: (abs(x), -x))  # Sort by absolute value, then by value (descending)
        return nums[0]  # Return the first element, which is the closest to zero
