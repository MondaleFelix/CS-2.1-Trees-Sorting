#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?

    # Best Case:
    TODO: Memory usage: ??? Why and under what conditions?"""



    # TODO: Check that all adjacent items are in order, return early if so
 
    # Items array is empty or contains one element
    if len(items) == 0 or len(items) == 1:
        return True

    # Returns False if previous number is larger than next
    for i in range(len(items) -1):
        if items[i] > items[i+1]:
            return False

    # Items array is sorted
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for i in range(len(items)):

        for j in range(0,len(items)-i-1):

            if items[j] > items[j+1]:
                items[j], items[j+1]= items[j+1], items[j]


    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
