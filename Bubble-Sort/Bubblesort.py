def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    
    Time Complexity: O(n^2) in worst and average cases, O(n) in best case
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list in ascending order
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize by detecting if array is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr


# Example usage and testing
if __name__ == "__main__":
    # Test case 1: Random array
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr1)
    print("Sorted array:", bubble_sort(test_arr1.copy()))
    print()
    
    # Test case 2: Already sorted array
    test_arr2 = [1, 2, 3, 4, 5]
    print("Original array:", test_arr2)
    print("Sorted array:", bubble_sort(test_arr2.copy()))
    print()
    
    # Test case 3: Reverse sorted array
    test_arr3 = [5, 4, 3, 2, 1]
    print("Original array:", test_arr3)
    print("Sorted array:", bubble_sort(test_arr3.copy()))
    print()
    
    # Test case 4: Array with duplicates
    test_arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Original array:", test_arr4)
    print("Sorted array:", bubble_sort(test_arr4.copy()))
