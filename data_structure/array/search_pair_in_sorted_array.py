import array

# Search a sorted array for a pair of values which sum up to a given number.


def search_pair(int_array, sum_value):
    index_1 = 0
    index_2 = len(int_array) - 1

    while index_1 < index_2:
        if (int_array[index_1] + int_array[index_2]) == sum_value:
            return True
        elif (int_array[index_1] + int_array[index_2]) > sum_value:
            index_2 -= 1
        else:
            index_1 += 1

    return False


if __name__ == '__main__':
    data = array.array('i', [1, 2, 3, 5, 6, 7, 8, 9, 10])
    print(search_pair(data, 11))
    print(search_pair(data, 20))
