# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Write a bubble sort that counts the number of comparisons and the number of exchanges made while sorting
# a list and returns a tuple of the two values (comparisons first, exchanges second). Do the same for insertion sort.
def bubble_count(a_list):
    comparisons = 0
    exchanges = 0
    n = len(a_list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1
            if a_list[j] > a_list[j + 1]:
                # Swap if elements are out of order
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                exchanges += 1

    return (comparisons, exchanges)


def insertion_count(a_list):
    comparisons = 0
    exchanges = 0

    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0:
            # Count comparison only when comparing list values
            comparisons += 1
            if a_list[pos] > value:
                # Shift element to the right if greater than value
                a_list[pos + 1] = a_list[pos]
                exchanges += 1
                pos -= 1
            else:
                break
        a_list[pos + 1] = value

    return (comparisons, exchanges)

# Example
# list1 = [5, 3, 1, 4, 2]
# bubble_results = bubble_count(list1.copy())
# insertion_results = insertion_count(list1.copy())
#
# print("Bubble Sort Results:", bubble_results)     # Output: (comparisons, exchanges)
# print("Insertion Sort Results:", insertion_results) # Output: (comparisons, exchanges)