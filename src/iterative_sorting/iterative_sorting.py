# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_performed = True
    while swap_performed:
        swap_performed = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_performed = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return []
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    output_arr = [0] * len(arr)
    counting_arr = [0] * (max(arr) + 1)
    for i in arr:
        counting_arr[i] += 1

    for j in range(0, len(counting_arr) - 1):
        counting_arr[j + 1] = counting_arr[j] + counting_arr[j + 1]
    # print(counting_arr, " <- counting array")
    for k in arr:
        # print(k, " <- current value")
        final_index = counting_arr[k] - 1
        output_arr[final_index] = k
        counting_arr[k] -= 1
    return output_arr

arr1 = [1, 5, 8, 4, -2, 9, 6, 0, 9, 3, 7]
print(arr1, " <- Original Array")
print(count_sort(arr1), " <- Sorted Array")
