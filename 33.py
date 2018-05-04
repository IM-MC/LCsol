def search(nums, target):

    lo = 0
    hi = len(nums)-1

    while lo < hi:
        mid = lo + (hi-lo)/2
        if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
            lo = mid + 1
        else:
            hi = mid

    return lo if target in nums[lo:lo+1] else -1

print(search([4,5,6,7,0,1,2], 0))
