# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i, j, k = 0, 0, 0
    if len(merged_arr) == 2:
        while i < len(arrA) and j < len(arrB):
            if arrA[i] < arrB[j]:
                merged_arr[k] = arrA[i]
                merged_arr[k + 1] = arrB[j]
                i += 1
                k += 1
            else:
                merged_arr[k] = arrB[j]
                merged_arr[k + 1] = arrA[i]
                j += 1
                k += 1
    else:
        while i < len(arrA) and j < len(arrB) and k < (len(merged_arr) - 1):
            if arrA[i] < arrB[j]:
                merged_arr[k] = arrA[i]
                i += 1
                k += 1
            else:
                merged_arr[k] = arrB[j]
                j += 1
                k += 1
        merged_arr[k:] = arrA[i:] + arrB[j:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        middle_index = len(arr) // 2
        left = merge_sort(arr[:middle_index])
        right = merge_sort(arr[middle_index:])
        return merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
