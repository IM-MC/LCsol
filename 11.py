def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    left = 0
    right = len(height) - 1
    max_area = 0

    for i in range(len(height)):
        max_height = min(height[left], height[right])
        x = right - left
        area = x * max_height
        if area > max_area:
            max_area = area

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area

print(maxArea([1,9,8]))
