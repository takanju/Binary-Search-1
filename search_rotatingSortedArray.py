class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :time complexity: O(logn)
        :space complexity: O(1)
        """
        if nums is None:
            return -1
        low =0
        high = len(nums) -1
        while(low<=high):
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]: # left sorted
                # check if target is in sorted part
                if nums[low] <= target and nums[mid]>target:
                    high=mid-1
                else:
                    low = mid+1
            else: # right sorted
                if nums[mid]< target and nums[high]>= target:
                    low=mid+1
                else:
                    high=mid-1
        return -1
            
        