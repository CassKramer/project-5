# Name: Cassandra Kramer
# OSU Email: kramecas@oregonstate.edu
# Course: CS261 - Data Structures/ Section
# Assignment: 5 MinHeap Implementation
# Due Date: 3/6/2023
# Description: Use dynamic array assignment to implement the complete binary tree heap

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to minheap while maintaining the heap property
        """
        self._heap._size += 1
        self._heap[self._heap.length() - 1] = node
        if self._heap.length() == self._heap._capacity:
            self._heap.resize(self._heap._capacity * 2)

        if self._heap.length() > 1:
            child = (self._heap.length()) - 1
            parent = (child - 1) // 2
            if self._heap.get_at_index(parent) > self._heap.get_at_index(child):
                self._heap._size += 1
                self._heap[self._heap.length() - 1] = self._heap[parent]
                self._heap.set_at_index(parent, self._heap[child])
                self._heap[self._heap.length() - 2] = self._heap[self._heap.length() - 1]
                child = parent
                parent = (child - 1) // 2


                while child != 0 and self._heap[parent] > self._heap[child]:
                   self._heap[self._heap.length() - 1] = self._heap[parent]
                   self._heap[parent] = self._heap[child]
                   self._heap[child] = self._heap[self._heap.length() - 1]
                   child = parent
                   parent = (child - 1) // 2

                self._heap._size -= 1

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty or false otherwise
        """
        if self._heap.length() == 0:
            return True
        else:
            return False

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it
        """
        if self._heap.length() == 0:
            raise MinHeapException
        if self._heap.length() == 1:
            return self._heap[0]
        min = self._heap[0]

        return min

    def remove_min(self) -> object:
        """
        Returns an object with the minimum key and removes it
        """
        if self._heap.length() == 0:
            raise MinHeapException
        if self._heap.length() == 1:
            min = self._heap[0]
            self._heap._size -= 1
            return min
        min = self._heap[0]

        index = 0
        self._heap[index] = self._heap[self._heap.length() - 1]

        _percolate_down(self._heap, index)
        return min



    def build_heap(self, da: DynamicArray) -> None:
        """
        overrides heap and uses dynamic array to build new heap
        """
        if self._heap.length() > da.length():
            self._heap._size -= self._heap.length() - da.length()
            for index in range(0, da.length()):
                self._heap[index] = da[index]



        if self._heap.length() < da.length():
            while self._heap._size < da.length():
                self._heap._size += 1
                if self._heap.length() == self._heap._capacity:
                    self._heap.resize(self._heap._capacity * 2)
            for index in range(0, da.length()):
                self._heap[index] = da[index]

        if self._heap.length() == da.length():
           for index in range(0, da.length()):
                self._heap[index] = da[index]


        parent = (self._heap.length() - 1) // 2
        child_1 = (parent * 2) + 1
        child_2 = (parent * 2) + 2

        if self._heap.length() == 2:
            if self._heap[parent] > self._heap[child_1]:
                value = self._heap[parent]
                self._heap[parent] = self._heap[child_1]
                self._heap[child_1] = value
                parent = -1

        if self._heap.length() <= 1:
            parent = -1



        while parent >= 0:

            if parent == 0:
                if self._heap[child_1] < self._heap[child_2]:
                    if self._heap[parent] > self._heap[child_1]:
                        value = self._heap[parent]
                        self._heap[parent] = self._heap[child_1]
                        self._heap[child_1] = value
                        parent = child_1
                        child_1 = (parent * 2) + 1
                        child_2 = (parent * 2) + 2

                    else:
                        parent = parent - 1
                        child_1 = (parent * 2) + 1
                        child_2 = (parent * 2) + 2

                elif self._heap[child_1] > self._heap[child_2]:
                    if self._heap[parent] > self._heap[child_2]:
                        value = self._heap[parent]
                        self._heap[parent] = self._heap[child_2]
                        self._heap[child_2] = value
                        parent = child_2
                        child_1 = (parent * 2) + 1
                        child_2 = (parent * 2) + 2



                    else:
                        parent = parent - 1
                        child_1 = (parent * 2) + 1
                        child_2 = (parent * 2) + 2

                elif self._heap[child_1] == self._heap[child_2]:
                    if self._heap[parent] > self._heap[child_1]:
                        value = self._heap[parent]
                        self._heap[parent] = self._heap[child_1]
                        self._heap[child_1] = value
                        parent = child_1
                        child_1 = (parent * 2) + 1
                        child_2 = (parent * 2) + 2

                    else:
                        parent = parent - 1
                        child_1 = (parent * 2) + 1
                        child_2 = (parent * 2) + 2

            elif child_1 > self._heap.length() - 1:
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

            elif child_2 > self._heap.length() - 1:
                if self._heap[parent] > self._heap[child_1]:
                    value = self._heap[parent]
                    self._heap[parent] = self._heap[child_1]
                    self._heap[child_1] = value
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2


            elif self._heap[child_1] < self._heap[child_2]:
                if self._heap[parent] > self._heap[child_1]:
                    value = self._heap[parent]
                    self._heap[parent] = self._heap[child_1]
                    self._heap[child_1] = value
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

            elif self._heap[child_1] > self._heap[child_2]:
                if self._heap[parent] > self._heap[child_2]:
                    value = self._heap[parent]
                    self._heap[parent] = self._heap[child_2]
                    self._heap[child_2] = value
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

            elif self._heap[child_1] == self._heap[child_2]:
                if self._heap[parent] > self._heap[child_1]:
                    value = self._heap[parent]
                    self._heap[parent] = self._heap[child_1]
                    self._heap[child_1] = value
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2


    def size(self) -> int:
        """
        Returns the number of items stored in the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap
        """
        self._heap._size = self._heap._size - self._heap._size


def heapsort(da: DynamicArray) -> None:
    """
    Sorts dynamic array in non-ascending order
    """
    parent = (da.length() - 1) // 2
    child_1 = (parent * 2) + 1
    child_2 = (parent * 2) + 2

    if da.length() == 2:
        if da[parent] > da[child_1]:
            value = da[parent]
            da[parent] = da[child_1]
            da[child_1] = value
            parent = -1

        else:
            parent = -1

    if da.length() <= 1:
        parent = -1

    while parent >= 0:

        if parent == 0:
            if da[child_1] < da[child_2]:
                if da[parent] > da[child_1]:
                    value = da[parent]
                    da[parent] = da[child_1]
                    da[child_1] = value
                    parent = child_1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

            elif da[child_1] > da[child_2]:
                if da[parent] > da[child_2]:
                    value = da[parent]
                    da[parent] = da[child_2]
                    da[child_2] = value
                    parent = child_2
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2



                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

            elif da[child_1] == da[child_2]:
                if da[parent] > da[child_1]:
                    value = da[parent]
                    da[parent] = da[child_1]
                    da[child_1] = value
                    parent = child_1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

                else:
                    parent = parent - 1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2

        elif child_1 > da.length() - 1:
            parent = parent - 1
            child_1 = (parent * 2) + 1
            child_2 = (parent * 2) + 2

        elif child_2 > da.length() - 1:
            if da[parent] > da[child_1]:
                value = da[parent]
                da[parent] = da[child_1]
                da[child_1] = value
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

            else:
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2


        elif da[child_1] < da[child_2]:
            if da[parent] > da[child_1]:
                value = da[parent]
                da[parent] = da[child_1]
                da[child_1] = value
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

            else:
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

        elif da[child_1] > da[child_2]:
            if da[parent] > da[child_2]:
                value = da[parent]
                da[parent] = da[child_2]
                da[child_2] = value
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

            else:
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

        elif da[child_1] == da[child_2]:
            if da[parent] > da[child_1]:
                value = da[parent]
                da[parent] = da[child_1]
                da[child_1] = value
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2

            else:
                parent = parent - 1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2



    count = da.length() - 1
    value = da[0]
    da[0] = da[count]
    da[da.length() - 1] = value
    count -= 1
    parent = 0
    child_1 = (2 * parent) + 1
    child_2 = (2 * parent) + 2
    for index in range(0, count):
        while count != 0:
            if child_1 >= count:
                if child_1 == 1:
                    count = 0

                else:
                    value = da[0]
                    da[0] = da[count]
                    da[count] = value
                    parent = 0
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                    count -= 1

            elif child_2 >= count:
                if da[parent] > da[child_1]:
                    value = da[parent]
                    da[parent] = da[child_1]
                    da[child_1] = value
                    parent = child_1
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                else:
                    value = da[0]
                    da[0] = da[count]
                    da[count] = value
                    parent = 0
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                    if da[count] <= da[parent]:
                        count -= 1

            elif da[child_1] < da[child_2]:
                if da[parent] > da[child_1]:
                    value = da[parent]
                    da[parent] = da[child_1]
                    da[child_1] = value
                    parent = child_1
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                else:
                    value = da[0]
                    da[0] = da[count]
                    da[count] = value
                    parent = 0
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                    if da[count] <= da[parent]:
                        count -= 1

            elif da[child_1] > da[child_2]:
                if da[parent] > da[child_2]:
                    value = da[parent]
                    da[parent] = da[child_2]
                    da[child_2] = value
                    parent = child_2
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2

                else:
                    value = da[0]
                    da[0] = da[count]
                    da[count] = value
                    parent = 0
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                    if da[count] <= da[parent]:
                        count -= 1


            elif da[child_1] == da[child_2]:
                if da[parent] > da[child_1]:
                    value = da[parent]
                    da[parent] = da[child_1]
                    da[child_1] = value
                    parent = child_1
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                else:
                    value = da[0]
                    da[0] = da[count]
                    da[count] = value
                    parent = 0
                    child_1 = (2 * parent) + 1
                    child_2 = (2 * parent) + 2
                    count -= 1
# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Percolates elements down the Minheap
    """

    da[parent] = da[da.length() - 1]
    child_1 = (2 * parent) + 1
    child_2 = (2 * parent) + 2

    while child_1 < da.length() - 1:

        if child_2 >= da.length() - 1:
            if da[child_1] < da[parent]:
                da[da.length() - 1] = da[parent]
                da[parent] = da[child_1]
                da[child_1] = da[da.length() - 1]
                da._size -= 1
                return

        if da[child_1] == da[child_2]:
            if da[child_1] < da[parent]:
                da[da.length() - 1] = da[parent]
                da[parent] = da[child_1]
                da[child_1] = da[da.length() - 1]
                parent = child_1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2
                if child_1 >= da.length() - 1:
                    da._size -= 1
                    return

            else:
                da._size -= 1
                return

        elif child_2 < da.length() - 1:

            if da[child_1] < da[child_2]:
                if da[child_1] < da[parent]:
                    da[da.length() - 1] = da[parent]
                    da[parent] = da[child_1]
                    da[child_1] = da[da.length() - 1]
                    parent = child_1
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2
                else:
                    da._size -= 1
                    return

            else:
                if da[child_2] < da[parent]:
                    da[da.length() - 1] = da[parent]
                    da[parent] = da[child_2]
                    da[child_2] = da[da.length() - 1]
                    parent = child_2
                    child_1 = (parent * 2) + 1
                    child_2 = (parent * 2) + 2
                else:
                    da._size -= 1
                    return

        else:
            if da[child_1] < da[parent]:
                da[da.length() - 1] = da[parent]
                da[parent] = da[child_1]
                da[child_1] = da[da.length() - 1]
                parent = child_1
                child_1 = (parent * 2) + 1
                child_2 = (parent * 2) + 2
            else:
                da._size -= 1
                return

    da._size -= 1
    return


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("\nPDF - build_heap example 2")
    print("--------------------------")
    da = DynamicArray([74254, -21172, 26882, -99117, 6434, -44371, 85667, -82964, -69627])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray([23362, 52005])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")


    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
