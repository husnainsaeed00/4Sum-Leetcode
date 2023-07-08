#The solution uses the concept of a four-pointer approach to find unique quadruplets that sum up to the target.
class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array in ascending order
        results = []  # Store the unique quadruplets
        
        for i in range(len(nums) - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                # Skip duplicate values for the second element
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                # Use two pointers approach for the remaining two elements
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    # Calculate the current sum
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum < target:
                        left += 1
                    elif curr_sum > target:
                        right -= 1
                    else:
                        # Found a quadruplet
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for the third element
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        # Skip duplicate values for the fourth element
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        # Move the pointers towards the center
                        left += 1
                        right -= 1
                        
        return results
