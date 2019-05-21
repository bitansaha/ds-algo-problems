import array
import sys

'''
Problem 1: Rearrange array such that a[i] = i
    Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. 
    If element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if 
    i is not present, display -1 at that place.
Source: https://www.geeksforgeeks.org/rearrange-array-arri/    
'''


# Solution 1:
# Time Complexity: O(n)
# Space Complexity: O(1)
def problem1_solution1(int_array):
    for index in range(len(int_array)):
        if index != int_array[index]:
            value = int_array[index]
            int_array[index] = -1
            while value != -1:
                temp = int_array[value]
                int_array[value] = value
                value = temp


# if __name__ == '__main__':
#     arr = [0, 14, 4, 7, 11, 12, -1, 13, 8, 2, 1, 5, 3, 6, -1, -1]
#     problem1_solution1(arr)
#     print(*arr)

''' -------------------------------------------------------------------------------------------------------------- '''

'''
Problem 2: Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
    Given an array of n elements. Our task is to write a program to rearrange the array such that elements at 
    even positions are greater than all elements before it and elements at odd positions are less than all elements 
    before it.
Source: https://www.geeksforgeeks.org/rearrange-array-arri-arrj-even-arri/
'''


# Solution 1: Using extra memory
# Time Complexity: O(n logn)
# Space Complexity: O(n)
def problem2_solution1(int_array):
    int_array_copy = int_array.copy()
    int_array_copy.sort()
    max_index = len(int_array_copy)
    min_index = -1
    for index in reversed(range(len(int_array))):
        if (index + 1) % 2 == 0:
            max_index -= 1
            int_array[index] = int_array_copy[max_index]
        else:
            min_index += 1
            int_array[index] = int_array_copy[min_index]


# Solution 2: Using modular arithmetic and no extra memory
# Time Complexity: O(n logn)
# Space Complexity: O(1)
def problem2_solution2(int_array):
    int_array.sort()
    max_value = int_array[len(int_array) - 1] + 1
    max_index = len(int_array)
    min_index = -1

    for index in reversed(range(len(int_array))):
        if (index + 1) % 2 == 0:
            max_index -= 1
            int_array[index] += (int_array[max_index] % max_value) * max_value
        else:
            min_index += 1
            int_array[index] += (int_array[min_index] % max_value) * max_value

    for index in range(len(int_array)):
        int_array[index] = int_array[index] // max_value


# if __name__ == '__main__':
#     original_arr = [1, 2, 1, 4, 5, 6, 8, 8]
#     arr = original_arr.copy()
#     problem2_solution1(arr)
#     print(*arr)
#     arr = original_arr.copy()
#     problem2_solution2(arr)
#     print(*arr)


''' -------------------------------------------------------------------------------------------------------------- '''

'''
Problem 3: Rearrange array such that it holds alternative positive and negative numbers. Positive on even indexes and 
    Negative on odd indexes. Number of positive and negative numbers need not be equal. If there are more positive 
    numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the 
    array. NO need to preserve the ORDER of the negative or positive numbers.
Source: https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/
'''


def swap(int_array, left_index, right_index):
    temp = int_array[left_index]
    int_array[left_index] = int_array[right_index]
    int_array[right_index] = temp


def negative_positive_split(int_array):
    left_index = 0
    right_index = len(int_array) - 1

    while left_index <= right_index:
        if int_array[left_index] >= 0 > int_array[right_index]:
            swap(int_array, left_index, right_index)

        if int_array[left_index] < 0:
            left_index += 1

        if int_array[right_index] >= 0:
            right_index -= 1

    return right_index


# Solution 1: Using extra memory
# Time Complexity: O(n)
# Space Complexity: O(n)
def problem3_solution1(int_array):
    int_array_copy = int_array.copy()
    negative_positive_split(int_array_copy)

    positive_index = len(int_array)
    negative_index = -1

    for index in range(len(int_array)):
        if index % 2 == 0:
            positive_index -= 1
            int_array[index] = int_array_copy[positive_index]
        else:
            negative_index += 1
            int_array[index] = int_array_copy[negative_index]


# Solution 2:
# Time Complexity: O(n)
# Space Complexity: O(1)
def problem3_solution2(int_array):
    negative_count = negative_positive_split(int_array)
    positive_index = negative_count + 1
    index = 0

    while index < len(int_array) and positive_index < len(int_array):
        if int_array[index] < 0:
            swap(int_array, index, positive_index)
            index += 2
            positive_index += 1
        else:
            break


# if __name__ == '__main__':
#     original_arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
#     arr = original_arr.copy()
#     problem3_solution1(arr)
#     print(*arr)
#     arr = original_arr.copy()
#     problem3_solution2(arr)
#     print(*arr)


''' -------------------------------------------------------------------------------------------------------------- '''

'''
Problem 4: Rearrange array such that it holds alternative positive and negative numbers. Positive on even indexes and 
    Negative on odd indexes. Number of positive and negative numbers need not be equal. If there are more positive 
    numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the 
    array. NEED to preserve the ORDER of the negative or positive numbers.
Source: https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
'''


# Solution 1: Using extra memory
# Time Complexity: O(n)
# Space Complexity: O(n)
def problem4_solution1(int_array):
    int_array_copy = int_array.copy()
    negative_index = 0
    positive_index = len(int_array) - 1

    for index in range(len(int_array)):
        if int_array[index] < 0:
            int_array_copy[negative_index] = int_array[index]
            negative_index += 1
        else:
            int_array_copy[positive_index] = int_array[index]
            positive_index -= 1

    negative_count = negative_index - 1
    negative_index = 0
    positive_index = len(int_array) - 1

    for index in range(len(int_array)):
        if index % 2 == 0:
            if positive_index > negative_count:
                int_array[index] = int_array_copy[positive_index]
                positive_index -= 1
            else:
                int_array[index] = int_array_copy[negative_index]
                negative_index += 1
        else:
            if negative_index <= negative_count:
                int_array[index] = int_array_copy[negative_index]
                negative_index += 1
            else:
                int_array[index] = int_array_copy[positive_index]
                positive_index -= 1


# Solution 2: Right Rotate
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def problem4_solution2(int_array):
    negative_index = -1
    positive_index = -1

    for index in range(len(int_array)):
        if index % 2 == 0 and int_array[index] < 0:
            next_positive_index = (positive_index if positive_index > index else index) + 1

            while next_positive_index < len(int_array):
                if int_array[next_positive_index] < 0:
                    next_positive_index += 1
                else:
                    right_rotate(int_array, index, next_positive_index)
                    positive_index = next_positive_index
                    break

            if next_positive_index >= len(int_array):
                break
        elif index % 2 > 0 and int_array[index] >= 0:
            next_negative_index = (negative_index if negative_index > index else index) + 1

            while next_negative_index < len(int_array):
                if int_array[next_negative_index] >= 0:
                    next_negative_index += 1
                else:
                    right_rotate(int_array, index, next_negative_index)
                    negative_index = next_negative_index
                    break

            if next_negative_index >= len(int_array):
                break


def right_rotate(int_array, left_index, right_index):
    temp = int_array[right_index]
    for index in range(right_index, left_index, -1):
        int_array[index] = int_array[index - 1]
    int_array[left_index] = temp


# Solution 3: Using modular arithmetic, to hold dual value in single index
# Time Complexity: O(n)
# Space Complexity: O(1)
def problem4_solution3(int_array):
    min_value = sys.maxsize
    max_value = -sys.maxsize - 1

    # retrieving the min, max values of the array
    for value in int_array:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    # adding the minimum value to all indexes to make it an array of positive integers
    for index in range(len(int_array)):
        int_array[index] -= min_value

    max_value = (max_value - min_value) + 1
    negative_index = -1
    positive_index = len(int_array)

    # using modular arithmetic in-place segregating negative and positive values
    for index in range(len(int_array)):
        value = int_array[index] % max_value
        if (value + min_value) < 0:
            # negative value encountered, place in next negative index
            negative_index += 1
            int_array[negative_index] += (value * max_value)
        else:
            # positive value encountered, place in next positive index
            positive_index -= 1
            int_array[positive_index] += (value * max_value)

    # clearing the old values and holding the segregated in-order negative, positive values
    for index in range(len(int_array)):
        int_array[index] = int_array[index] // max_value

    negative_count = negative_index
    negative_index = -1
    positive_index = len(int_array)

    for index in range(len(int_array)):
        if index % 2 == 0:
            if (positive_index - 1) > negative_count:
                positive_index -= 1
                int_array[index] += (int_array[positive_index] % max_value) * max_value
            else:
                negative_index += 1
                int_array[index] += (int_array[negative_index] % max_value) * max_value
        else:
            if (negative_index + 1) <= negative_count:
                negative_index += 1
                int_array[index] += (int_array[negative_index] % max_value) * max_value
            else:
                positive_index -= 1
                int_array[index] += (int_array[positive_index] % max_value) * max_value

    # retaining the new positive negative order and getting the old values back
    for index in range(len(int_array)):
        int_array[index] = (int_array[index] // max_value) + min_value


# if __name__ == '__main__':
#     original_arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
#     arr = original_arr.copy()
#     problem4_solution1(arr)
#     print(*arr)
#     arr = original_arr.copy()
#     problem4_solution2(arr)
#     print(*arr)
#     arr = original_arr.copy()
#     problem4_solution3(arr)
#     print(*arr)


''' -------------------------------------------------------------------------------------------------------------- '''

'''
Problem 5: Move all zeros to the end of array.
Source: https://www.geeksforgeeks.org/move-zeroes-end-array-set-2-using-single-traversal/
'''


def problem5_solution1(int_array):
    zero_count = 0
    for index in range(len(int_array)):
        if int_array[index] == 0:
            zero_count += 1
        else:
            int_array[index - zero_count] = int_array[index]
            if zero_count > 0:
                int_array[index] = 0


if __name__ == '__main__':
    original_arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    arr = original_arr.copy()
    problem5_solution1(arr)
    print(*arr)
