def bubble_sort(nums):
    
    n = len(nums)
    for i in range(n):
        # Flag to check if any swapping happens in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap the elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        # If no two elements were swapped, the list is sorted
        if not swapped:
            break
    return nums

