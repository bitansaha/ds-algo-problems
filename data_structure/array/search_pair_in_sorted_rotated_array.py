import array


# Search a sorted rotated array for a pair of values which sum up to a given number.

def search_pair(int_array, sum_value):
    pivot = search_pivot(int_array)
    start_index = (pivot + 1) % len(int_array)
    end_index = pivot

    while start_index != end_index:

        if (int_array[start_index] + int_array[end_index]) == sum_value:
            return True
        elif (int_array[start_index] + int_array[end_index]) > sum_value:
            end_index = (end_index - 1) % len(int_array)
        else:
            start_index = (start_index + 1) % len(int_array)

    return False


def search_pivot(int_array):
    if not int_array:
        raise Exception('Empty Array')

    pivot = 0

    if len(int_array) == 1:
        return pivot

    start_index = pivot + 1
    end_index = len(int_array) - 1

    while start_index <= end_index:
        mid = start_index + (end_index - start_index)//2

        if int_array[mid] > int_array[pivot]:
            pivot = mid
            start_index = mid + 1
        else:
            end_index = mid - 1

    return pivot


if __name__ == '__main__':
    data = array.array('i', [8, 9, 10, 1, 2, 3, 5, 6, 7])
    print(search_pair(data, 11))
    print(search_pair(data, 20))