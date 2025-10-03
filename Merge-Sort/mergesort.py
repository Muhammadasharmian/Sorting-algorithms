def merge_sort(arr):
    """
    Merge Sort Algorithm
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n)
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    
    Args:
        left: Sorted list
        right: Sorted list
    
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0
    
    # Compare elements from left and right arrays and add smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right array
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


# Example usage and testing
if __name__ == "__main__":
    # Test case 1: Random array
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr1)
    print("Sorted array:", merge_sort(test_arr1))
    print()
    
    # Test case 2: Already sorted array
    test_arr2 = [1, 2, 3, 4, 5]
    print("Original array:", test_arr2)
    print("Sorted array:", merge_sort(test_arr2))
    print()
    
    # Test case 3: Reverse sorted array
    test_arr3 = [5, 4, 3, 2, 1]
    print("Original array:", test_arr3)
    print("Sorted array:", merge_sort(test_arr3))
    print()
    
    # Test case 4: Array with duplicates
    test_arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Original array:", test_arr4)
    print("Sorted array:", merge_sort(test_arr4))
    print()
    
    # Test case 5: Empty array
    test_arr5 = []
    print("Original array:", test_arr5)
    print("Sorted array:", merge_sort(test_arr5))
    print()
    
    # Test case 6: Single element
    test_arr6 = [42]
    print("Original array:", test_arr6)
    print("Sorted array:", merge_sort(test_arr6))
