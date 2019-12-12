def max_end3(nums):
  changeValue = 0
  if nums[0] > nums[-1]:
    changeValue = nums[0]
    nums[1] = changeValue
    nums[-1] = changeValue
    return nums
  elif nums[-1] > nums[0]:
    changeValue = nums[-1]
    nums[0] = changeValue
    nums[1] = changeValue
    return nums
  elif nums[0] == nums[1] and nums[1] == nums[-1]:
    return nums
  elif nums[0] == nums[-1]:
    nums[1] = nums[-1]
    return nums
