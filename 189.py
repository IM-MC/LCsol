
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    def numReverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k = k%len(nums)

    if k:
        numReverse(0, len(nums)-1)
        numReverse(0, k-1)
        numReverse(k, len(nums)-1)
    




arr = [1,2,3,4]
rotate(arr, 1)
print(arr)