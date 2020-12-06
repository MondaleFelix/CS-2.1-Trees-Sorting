#!python

from sorting_iterative import bubble_sort
from random import randint


def merge(items1, items2):
	"""Merge given lists of items, each assumed to already be in sorted order,
	and return a new list containing all items in sorted order.

	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""

	sorted_list = []
	items1_index = 0
	items2_index = 0

	# TODO: Repeat until one list is empty

	while items1_index < len(items1) and items2_index < len(items2):

	# TODO: Find minimum item in both lists and append it to new list
		if items1[items1_index] > items2[items2_index]:
			sorted_list.append(items2[items2_index])
			items2_index += 1
		else:
			sorted_list.append(items1[items1_index])
			items1_index += 1	

	# TODO: Append remaining items in non-empty list to new list
	sorted_list += items1[items1_index:]
	sorted_list += items2[items2_index:]

	return sorted_list
print(merge([5],[3]))

def split_sort_merge(items):
	"""Sort given items by splitting list into two approximately equal halves,
	sorting each with an iterative sorting algorithm, and merging results into
	a list in sorted order.
	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""

	# Return arr if empty or has one item
	if len(items) == 1 or len(items) == 0:
		return items

	# TODO: Split items list into approximately equal halves
	middle = len(items) // 2

	left = items[:middle]
	right = items[middle:]

	# TODO: Sort each half using any other sorting algorithm
	bubble_sort(left)
	bubble_sort(right)

	# TODO: Merge sorted halves into one list in sorted order

	sorted_list = merge(left,right)
	return sorted_list

# print(split_sort_merge([1,4,7,2,4,3,8,5,2,5,3,6]))

def merge_sort(items):
	"""Sort given items by splitting list into two approximately equal halves,
	sorting each recursively, and merging results into a list in sorted order.
	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""


	# TODO: Check if list is so small it's already sorted (base case)

	if len(items) == 1 or len(items) == 0:
		return items

	# TODO: Split items list into approximately equal halves
	else:

		middle = len(items) // 2
		left = items[:middle]
		right = items[middle:]

	# TODO: Sort each half by recursively calling merge sort
		merge_sort(left)
		merge_sort(right)
	# TODO: Merge sorted halves into one list in sorted order
		items[:] = merge(left, right)

	return items


# Helper method to peform in place swap
def swap(items, i, j):
    tmp = items[i]
    items[i] = items[j]
    items[j] = tmp


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot with median of 3 function from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    swap(items, low, randint(low, high))
    pivot = low

    left = low + 1
    right = high

    while True:
        # Find item greater than pivot
        while left <= right and items[left] <= items[pivot]:
            left += 1

        # Find item less than pivot
        while left <= right and items[right] >= items[pivot]:
            right -= 1

        # Still in bounds, swap items 
        if left <= right:
            swap(items, left, right)
        else:
            break

    #Move pivot to final position
    swap(items, right, pivot)
    return right


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # start quicksort
    if low == None and high == None:
        low = 0
        high = len(items) - 1

    # Base case input is too small
    if low < high:
        # partition items
        pivot = partition(items, low, high)

        # sort left sublist
        quick_sort(items, low, pivot - 1)
    
        # sort right sublist
        quick_sort(items, pivot + 1, high)    