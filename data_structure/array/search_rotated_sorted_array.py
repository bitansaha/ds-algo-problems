import array


def search_pivot(int_array):
    pivot = 0

    if len(int_array) == 1:
        return pivot

    start_index = pivot + 1
    end_index = len(int_array) - 1

    while 1:
        if start_index > end_index:
            break

        mid = start_index + (end_index - start_index) // 2

        if int_array[mid] > int_array[pivot]:
            pivot = mid
            start_index = mid + 1
        else:
            end_index = mid - 1

    return pivot


def binary_search(int_array, start_index, end_index, search_term):
    if start_index > end_index:
        return -1

    mid = start_index + (end_index - start_index) // 2

    if int_array[mid] == search_term:
        return mid

    if int_array[mid] < search_term:
        return binary_search(int_array, mid + 1, end_index, search_term)
    else:
        return binary_search(int_array, start_index, mid - 1, search_term)


def search_rotated_sorted_array(int_array, search_term):
    pivot = search_pivot(int_array)
    return binary_search(int_array, 0, pivot, search_term) if search_term > int_array[0] \
        else binary_search(int_array, pivot + 1, len(int_array) - 1, search_term)


if __name__ == '__main__':
    data = array.array('i', [5, 6, 7, 8, 9, 10, 1, 2, 3])
    print(search_rotated_sorted_array(data, 3))
