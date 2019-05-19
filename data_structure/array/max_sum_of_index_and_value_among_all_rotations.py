import array


# Problem: Rotate the array as many times as required and return the maximum possible of summation of i*arr[i]
# Reference: https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/

def find_max_sum_of_value_and_index(int_array):
    value_sum = 0
    current_index_value_sum = 0

    for index in range(len(int_array)):
        value_sum += int_array[index]
        current_index_value_sum += index * int_array[index]

    max_index_value_sum = current_index_value_sum

    for rotation_index in range(1, len(int_array)):
        previous_index_value_sum = current_index_value_sum
        current_index_value_sum = previous_index_value_sum + (value_sum - len(int_array) * int_array[len(int_array) -
                                                                                                     rotation_index])
        max_index_value_sum = max(max_index_value_sum, current_index_value_sum)

    return max_index_value_sum


if __name__ == '__main__':
    data = array.array('i', [10, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(find_max_sum_of_value_and_index(data))
