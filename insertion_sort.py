#Python program for the Insertion Sort Algorithm that sorts in monotonically decreasing order.

#Function to sort in descending order using Insertion Sort
def insertion_sort_in_dec_order(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    print("--------------------------------------------------------")
    print("\n--- Sorting in decreasing order using Insertion Sort ---\n")
    print("--------------------------------------------------------")
    # Example 1
    data1 = [5, 2, 9, 9, 3, 6]
    print("Original data:", data1)
    print("Sorted: ", insertion_sort_in_dec_order(data1))
    print()
    # Example 2
    data2 = [1, 4, 3, 2, 5]
    print("Original data:", data2)
    print("Sorted: ", insertion_sort_in_dec_order(data2))
    print()
    # Example 3
    data3 = [10, 20, 30, 40, 50]
    print("Original data:", data3)
    sorted_data = insertion_sort_in_dec_order(data3)
    print("Sorted: ", sorted_data)
    print("--------------------------------------------------------")