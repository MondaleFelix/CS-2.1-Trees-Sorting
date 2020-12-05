#!python

from sorting_iterative import bubble_sort

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

print(merge_sort([5,7,3]))





def partition(items, low, high):
	"""Return index `p` after in-place partitioning given items in range
	`[low...high]` by choosing a pivot (TODO: document your method here) from
	that range, moving pivot into index `p`, items less than pivot into range
	`[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Choose a pivot any way and document your method in docstring above
	# TODO: Loop through all items in range [low...high]
	# TODO: Move items less than pivot into front of range [low...p-1]
	# TODO: Move items greater than pivot into back of range [p+1...high]
	# TODO: Move pivot item into final position [p] and return index p
	pass


def quick_sort(items, low=None, high=None):
	"""Sort given items in place by partitioning items in range `[low...high]`
	around a pivot item and recursively sorting each remaining sublist range.
	TODO: Best case running time: ??? Why and under what conditions?
	TODO: Worst case running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Check if high and low range bounds have default values (not given)
	# TODO: Check if list or range is so small it's already sorted (base case)
	# TODO: Partition items in-place around a pivot and get index of pivot
	# TODO: Sort each sublist range by recursively calling quick sort
	pass