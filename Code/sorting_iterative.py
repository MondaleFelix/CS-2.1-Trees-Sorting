#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?

    # Best Case: O(1) If given array is empty or has one item
    # Worst Case: O(n) If all items in the array are unsorted

    TODO: Memory usage: ??? Why and under what conditions?"""
    # O(1) Being sorted in place so no new memory is being created


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
    
    # O(n^2) If all elements are unsorted

    TODO: Memory usage: ??? Why and under what conditions?"""
    # O(1) No extra mememory is being created

    # Iterate however many items there are in the list
    for i in range(len(items)):

        # Iterate from current element to end of list
        for j in range(0,len(items)-i-1):

            # Swap if current element is larger than second element
            if items[j] > items[j+1]:
                items[j], items[j+1]= items[j+1], items[j]


    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?

    # O(n^2) If all elements are unsorted

    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    # Iterate through list of items
    for i in range(len(items)):

        # Keeps track of lowest amount index
        min_index = i

        # Compares minimum number with other numbers
        for j in range(i+1, len(items)):

            # reassigns minimum index
            if items[min_index] > items[j]:
                min_index = j 
              
        # Performs swap
        items[i], items[min_index] = items[min_index], items[i] 

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

        # Traverse through 1 to len(arr) 
    for i in range(1, len(items)): 
  
        key = items[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < items[j] : 
                items[j + 1] = items[j] 
                j -= 1
        items[j + 1] = key 



