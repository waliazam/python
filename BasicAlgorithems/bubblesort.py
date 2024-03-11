'''
Bubble Sort is a simple comparison-based algorithm in which each pair of adjacent
elements is compared, and the elements are swapped if they are not in order. 
This process is repeated until the list is sorted.

'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # Outer loop for the number of passes
        for j in range(0, n-i-1):  # Inner loop for each pass
            if arr[j] > arr[j+1]:  # Compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if the element on the left is greater than the right
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
