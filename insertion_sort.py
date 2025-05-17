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
    data = [5, 2, 9, 9, 3, 6]
    sorted_data = insertion_sort_in_dec_order(data)
    print("Sorted in decreasing order:", sorted_data)