# Array Problems and Solutions
import array
import math


# Problem 1: Rotate Array


class RotateArray:
    def rotate_left(self, int_array, rotate_count):
        pass

    def rotate_right(self, int_array, rotate_count):
        pass


# Solution 1: Uses the Python Slice and dual allocation to rotate the new array. Internally it probably uses memory
# to hold intermediate data.
# Time Complexity: O(n)
# Space Complexity: O(n)
class SliceBasedArrayRotation(RotateArray):
    def rotate_left(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        int_array[len(int_array) - _rotate_count: len(int_array)], int_array[0: len(int_array) - _rotate_count] = \
            int_array[0: _rotate_count], int_array[_rotate_count: len(int_array)]
        return int_array

    def rotate_right(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        int_array[len(int_array) - (len(int_array) - _rotate_count): len(int_array)], int_array[0: len(int_array) - (
                len(int_array) - _rotate_count)] = \
            int_array[0: len(int_array) - _rotate_count], int_array[len(int_array) - _rotate_count: len(int_array)]
        return int_array


# Solution 2: Using extra memory
# Time Complexity: O(n)
# Space Complexity: O(n)
class MemoryBasedArrayRotation(RotateArray):
    def rotate_left(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        temp_memory = []
        for index in range(len(int_array)):
            if index < _rotate_count:
                temp_memory.append(int_array[index])
            int_array[index] = int_array[index + _rotate_count] if index + _rotate_count < len(int_array) \
                else temp_memory[(index + _rotate_count) - len(int_array)]
        return int_array

    def rotate_right(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        temp_memory = []
        for index in range(len(int_array)):
            if index < (len(int_array) - _rotate_count):
                temp_memory.append(int_array[index])
            int_array[index] = int_array[index + (len(int_array) - _rotate_count)] if (index + (
                    len(int_array) - _rotate_count)) < len(int_array) \
                else temp_memory[(index + (len(int_array) - _rotate_count)) - len(int_array)]
        return int_array


# Solution 3: Rotate the full array 'n' number of times where 'n' is the required indexes to be rotated.
# Time Complexity: O(n*n)
# Space Complexity: O(1)
class LoopBasedArrayRotation(RotateArray):
    def rotate_left(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        for rotate_index in range(_rotate_count):
            temp_variable = int_array[len(int_array) - 1]
            for index in range(len(int_array) - 1, -1, -1):
                swap_variable = int_array[index - 1 if index - 1 >= 0 else len(int_array) - 1]
                int_array[index - 1 if index - 1 >= 0 else len(int_array) - 1] = temp_variable
                temp_variable = swap_variable
        return int_array

    def rotate_right(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        for rotate_index in range(_rotate_count):
            temp_variable = int_array[0]
            for index in range(len(int_array)):
                swap_variable = int_array[index + 1 if index + 1 < len(int_array) else 0]
                int_array[index + 1 if index + 1 < len(int_array) else 0] = temp_variable
                temp_variable = swap_variable
        return int_array


# Solution 4: Rotate array by reversing the first half and second half and then reversing the whole array
# Time Complexity: O(n)
# Space Complexity: O(1)
class ReversalBasedArrayRotation(RotateArray):
    def rotate_left(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        # reverse left side
        self.__reverse_int_array(int_array, 0, _rotate_count)

        # reverse right side
        self.__reverse_int_array(int_array, _rotate_count, len(int_array))

        # reverse the whole array
        self.__reverse_int_array(int_array, 0, len(int_array))

        return int_array

    def rotate_right(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        # reverse left side
        self.__reverse_int_array(int_array, 0, len(int_array) - _rotate_count)

        # reverse right side
        self.__reverse_int_array(int_array, len(int_array) - _rotate_count, len(int_array))

        # reverse the whole array
        self.__reverse_int_array(int_array, 0, len(int_array))

        return int_array

    def __reverse_int_array(self, int_array, start_index, end_index):
        for left_index in range(start_index, end_index):
            right_index = start_index + (end_index - start_index - 1 - (left_index - start_index))
            if right_index <= left_index:
                break
            temp_value = int_array[left_index]
            int_array[left_index] = int_array[right_index]
            int_array[right_index] = temp_value


# Solution 5: Juggling algorithm based on GCD
# Time Complexity: O(n)
# Space Complexity: O(1)
class GCDBasedArrayRotation(RotateArray):
    def rotate_left(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        for gcd_index in range(math.gcd(len(int_array), _rotate_count)):
            start_index = gcd_index
            start_index_value = int_array[gcd_index]
            value_insert_index = gcd_index
            value_fetch_index = gcd_index
            while True:
                value_fetch_index = value_insert_index + _rotate_count
                value_fetch_index = value_fetch_index if value_fetch_index < len(int_array) \
                    else value_fetch_index - len(int_array)
                if value_fetch_index == start_index:
                    break
                int_array[value_insert_index] = int_array[value_fetch_index]
                value_insert_index = value_fetch_index

            int_array[value_insert_index] = start_index_value

            return int_array

    def rotate_right(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        for gcd_index in range(math.gcd(len(int_array), _rotate_count)):
            start_index = len(int_array) - 1 - gcd_index
            start_index_value = int_array[len(int_array) - 1 - gcd_index]
            value_insert_index = len(int_array) - 1 - gcd_index
            value_fetch_index = len(int_array) - 1 - gcd_index
            while True:
                value_fetch_index = value_insert_index - _rotate_count
                value_fetch_index = value_fetch_index if value_fetch_index >= 0 \
                    else value_fetch_index + len(int_array)
                if value_fetch_index == start_index:
                    break
                int_array[value_insert_index] = int_array[value_fetch_index]
                value_insert_index = value_fetch_index

            int_array[value_insert_index] = start_index_value

            return int_array


class BlockSwapBasedArrayRotation(RotateArray):
    def rotate_left(self, int_array, rotate_count):
        _rotate_count = rotate_count % len(int_array)
        start_index = 0
        end_index = len(int_array) - 1

        return self.__rotate(int_array, start_index, end_index, rotate_count)

    def __rotate(self, int_array, start_index, end_index, rotate_count):
        array_1_start_index = start_index
        array_1_end_index = array_1_start_index + rotate_count - 1
        array_2_start_index = array_1_end_index + 1
        array_2_end_index = end_index
        array_1_size = array_1_end_index + 1 - array_1_start_index
        array_2_size = array_2_end_index + 1 - array_2_start_index

        if array_1_size == array_2_size:
            return self.__swap(int_array, array_1_start_index, array_2_start_index, rotate_count)
        elif array_1_size < array_2_size:
            self.__swap(int_array, array_1_start_index, array_2_end_index + 1 - rotate_count, rotate_count)
            return self.__rotate(int_array, start_index, end_index - rotate_count, rotate_count)
        else:
            _rotate_count = array_2_end_index + 1 - array_1_start_index - rotate_count
            self.__swap(int_array, array_1_start_index, array_2_end_index, _rotate_count)
            return self.__rotate(int_array, start_index + rotate_count, end_index, _rotate_count)

    def __swap(self, int_array, array_1_start_index, array_2_start_index, array_size):
        for index in range(array_size):
            temp = int_array[array_1_start_index + index]
            int_array[array_1_start_index + index] = int_array[array_2_start_index + index]
            int_array[array_2_start_index + index] = temp
        return int_array


if __name__ == '__main__':
    func_map = dict(
        slice_and_rotate_array=SliceBasedArrayRotation(),
        rotate_array_using_memory=MemoryBasedArrayRotation(),
        rotate_array_by_each_index=LoopBasedArrayRotation(),
        rotate_array_by_reversal_strategy=ReversalBasedArrayRotation(),
        rotate_array_by_juggling_algorithm=GCDBasedArrayRotation(),
        rotate_array_by_block_swap=BlockSwapBasedArrayRotation()
    )

    for algorithm_name, rotate_algorithm in func_map.items():
        print('Algorithm: ', algorithm_name, '\n', end=' ', flush=True)
        print('Rotate Left: ', rotate_algorithm.rotate_left(array.array('i', [1, 2, 3, 4, 5, 6, 7]), 2), '\n', end=' ', flush=True)
        print('Rotate Right: ', rotate_algorithm.rotate_right(array.array('i', [1, 2, 3, 4, 5, 6, 7]), 2), '\n', end=' ',
              flush=True)
        print('', '\n', end=' ', flush=True)
