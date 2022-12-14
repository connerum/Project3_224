# GROUP: Conner Um & Landen Finlinson

import unittest
import math

""" A HeapSort module. For more information on how to implement the functions, refer to 
+ CLRS3, chapter 6: the module's organization follows the text's exposition faithfully.
+ The slides for this course "Heaps: the Owner's Manual": they contain a few useful tips about the Python implementation.
"""


########### DO NOT MODIFY ####################
class HeapCapable(list):
    """
    A HeapCapable object is just a normal Python list, with an extra `heap_size` field. For conveniency, this type is used throughout the module for all arrays, even if they are not actually max-heaps.
    .. warning:: Do not modify this class.
    """

    def __init__(self, lst):
        """
        Initializes a new heap from a list.
        """
        super().__init__(lst)  # calling the superclass (list) constructor
        self.heap_size = len(self)


############ ASSIGNMENT STARTS HERE #########

def left(i):
    """
    Return the left child of the given node.

    The procedure is just an arithmetical computation of the L child's index. Checking that such a child exists is left to the caller function.
        .. note:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted (the slides "Heaps: the Owner's manual" tell you how).

    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's left child
    :rtype: int
        """
    return 2 * i + 1


def right(i):
    """
    Return the right child of the given node.
    The procedure is just an arithmetical computation of the R child's index. Checking that such a child exists is left to the caller function.
     .. note:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted (the slides "Heaps: the Owner's manual" tell you how).

    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's right child
    :rtype: int
    """
    return 2 * (i + 1)


def parent(i):
    """
    Return the parent of the given node.
    The procedure is just an arithmetical computation of the parent's index. Checking that such a parent exists is left to the caller function.

     .. note:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted (the slides "Heaps: the Owner's manual" tell you how).
    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's parent
    :rtype: int
    """
    return math.floor((i - 1) / 2)


def max_heapify(A, i):
    """
    Given an array A, and assuming that the subtrees rooted at A[i]'s L and R children are max-heaps, restore the max-heap property.
        .. note:: The procedure does not return anything: it simply modifies the array in place.

    :param A: an array.
    :param i: the index of the  node to be floated down
    :type A: heapsort_skeleton.HeapCapable
    :type i: int
    """
    l = left(i)
    r = right(i)

    largest = i
    if l < A.heap_size and A[l] > A[i]:
        largest = l
    if r < A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    """ Build a max-heap, from an unsorted array. 

        .. note:: The procedure does not return anything: it modifies the array in place.
    :param A: the array to be sorted.
    :type A: heapsort_skeleton.HeapCapable
    """
    A.heap_size = len(A)
    for i in range(math.floor((len(A) / 2)), -1, -1):
        max_heapify(A, i)


def HeapSort(A):
    """ Sort the array in place.

    .. note:: The function sorts in place, and therefore does not return anything.
    :param A: an array, with values in random order - do not assume that the array is already a max-heap! The `build_max_heap` procedure needs to be run on A before the actual sorting takes place.
    :type A: heapsort_skeleton.HeapCapable
    """
    build_max_heap(A)
    for i in range((len(A) - 1), 0, -1):
        A[0], A[i] = A[i], A[0]
        A.heap_size -= 1
        max_heapify(A, 0)


def Insert(A, x):
    """ Inserts the element, x, into the array A

        :param A: an array.
        :param x: the element to be added
        :type A: heapsort_skeleton.HeapCapable
        :type x: int
        """
    A.append(x)


def Maximum(A):
    """ Return the maximum element in array A

    :param A: an array.
    :type A: heapsort_skeleton.HeapCapable
    :return: the maximum value in array A
    :rtype: int
    """
    if len(A) != 0:
        return A[0]


def Extract_Max(A):
    """ Delete the Maximum element from array A then return the maximum element in array A

        :param A: an array.
        :type A: heapsort_skeleton.HeapCapable
        :return: the maximum value in array A
        :rtype: int
        """
    if len(A) != 0:
        maxValue = A[0]
        del A[0]
        A.insert(0, A.pop())
        return maxValue




def Increase_Key(A, x, k):
    """ Increases value of node x to value of k as long as it is greater

        :param A: an array.
        :param x: the element to be increased
        :param k: the desired value to increase to
        :type A: heapsort_skeleton.HeapCapable
        :type x: int
        :type k: int
        """
    element = A[x-1]
    if k > element:
        A[x-1] = k


############# DO NOT MODIFY ##############################
class testHeapSort(unittest.TestCase):
    def test_insert_1(self):
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
        build_max_heap(A)
        Insert(A, 5)
        build_max_heap(A)
        self.assertEqual(A, [27, 17, 10, 16, 13, 9, 5, 5, 7, 12, 4, 8, 3, 0, 1])
    def test_insert_2(self):
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        Insert(A, 15)
        build_max_heap(A)
        self.assertEqual(A, [19, 17, 18, 16, 10, 6, 15, 13, 1, 8, 5, 4, 2, 3, 12])
    def test_insert_emtpy_3(self):
        A = HeapCapable([])
        build_max_heap(A)
        Insert(A, 3)
        build_max_heap(A)
        self.assertEqual(A, [3])

    def test_maximum_endofarray_1(self):
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 51])
        build_max_heap(A)
        self.assertEqual(Maximum(A), 51)
    def test_maximum_startofarray_2(self):
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        self.assertEqual(Maximum(A), 19)
    def test_maximum_emptyarray_3(self):
        A = HeapCapable([])
        build_max_heap(A)
        self.assertEqual(Maximum(A), None)

    def test_extractMaximumReturn_1(self):
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
        build_max_heap(A)
        self.assertEqual(Extract_Max(A), 27)
    def test_extractMaximumReturn_2(self):
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        self.assertEqual(Extract_Max(A), 19)
    def test_extractMaximumReturn_empty_3(self):
        A = HeapCapable([])
        build_max_heap(A)
        self.assertEqual(Extract_Max(A), None)
    def test_extractMaximumRemove_bestcase_1(self):
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
        build_max_heap(A)
        Extract_Max(A)
        build_max_heap(A)
        self.assertEqual(A, [17, 16, 10, 7, 13, 9, 1, 5, 0, 12, 4, 8, 3])
    def test_extractMaximumRemove_2(self):
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        Extract_Max(A)
        build_max_heap(A)
        self.assertEqual(A, [18, 17, 12, 16, 10, 6, 3, 13, 1, 8, 5, 4, 2])
    def test_extractMaximumRemove_3(self):
        A = HeapCapable([5, 1, 17, 8, 9, 22, 2, 0])
        build_max_heap(A)
        Extract_Max(A)
        build_max_heap(A)
        self.assertEqual(A, [17, 9, 5, 8, 1, 0, 2])

    def test_increasekey_bestcase_1(self):
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
        build_max_heap(A)
        Increase_Key(A, 8, 20)
        build_max_heap(A)
        self.assertEqual(A[1], 20)
    def test_increasekey_smallervalue_2(self):
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        Increase_Key(A, 5, 4)
        build_max_heap(A)
        self.assertEqual(A[4], 10)
    def test_increasekey_largerroot_3(self):
        A = HeapCapable([5, 1, 2, 17, 8, 9, 22, 2, 0])
        build_max_heap(A)
        Increase_Key(A, 1, 25)
        build_max_heap(A)
        self.assertEqual(A[0], 25)

    def test_left_1(self):
        self.assertEqual(left(0), 1)

    def test_left_2(self):
        self.assertEqual(left(2), 5)

    def test_left_3(self):
        self.assertEqual(left(3), 7)

    def test_right_1(self):
        self.assertEqual(right(0), 2)

    def test_right_2(self):
        self.assertEqual(right(2), 6)

    def test_right_3(self):
        self.assertEqual(right(3), 8)

    def test_parent_1(self):
        self.assertEqual(parent(1), 0)

    def test_parent_2(self):
        self.assertEqual(parent(2), 0)

    def test_parent_3(self):
        self.assertEqual(parent(3), 1)

    def test_parent_4(self):
        self.assertEqual(parent(4), 1)

    def test_max_heapify_general_case(self):
        """ 
        CLRS3, exercise 6.2-1
        """
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
        max_heapify(A, 2)
        self.assertEqual(A, [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])

    def test_max_heapify_untouched(self):
        """ 
        MaxHeapify() does not change the array if A[i] is larger than its two children
        """
        A = HeapCapable([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
        max_heapify(A, 1)
        self.assertEqual(A, [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])

    def test_max_heapify_reduced_heap_size(self):
        """ 
        Max-Heapify() should always check against the heap's size, not the array's length!
        """
        A = HeapCapable([3, 10, 7, 9, 7, 5, 2, 8, 5, 4])
        A.heap_size = 7
        max_heapify(A, 0)
        self.assertEqual(A, [10, 9, 7, 3, 7, 5, 2, 8, 5, 4])

    def test_buildmaxheap_unique_values(self):
        """
        BuildMaxHeap: general case, with non-repeated values
        """
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        self.assertEqual(A, [19, 17, 18, 16, 10, 6, 12, 13, 1, 8, 5, 4, 2, 3])

    def test_buildmaxheap_repeated_values(self):
        """
        BuildMaxHeap: general case, with repeated values
        """
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
        build_max_heap(A)
        self.assertEqual(A, [18, 16, 17, 10, 12, 13, 7, 3, 4, 7, 8, 8, 7, 3])

    def test_buildmaxheap_1_element_array(self):
        """
        BuildMaxHeap: special case - 1-element array
        """
        A = HeapCapable([7])
        build_max_heap(A)
        self.assertEqual(A, [7])

    def test_heapsort_unique_values(self):
        """
        HeapSort: general case, with unique values
        """
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        HeapSort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 16, 17, 18, 19])

    def test_heapsort_repeated_values(self):
        """
        HeapSort: general case, with repeated values
        """
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
        HeapSort(A)
        self.assertEqual(A, [3, 3, 4, 7, 7, 7, 8, 8, 10, 12, 13, 16, 17, 18])

    def test_heapsort_1_element_array(self):
        """
        HeapSort: special case - 1-element array
        """
        A = HeapCapable([7])
        HeapSort(A)
        self.assertEqual(A, [7])


def main():
    unittest.main()


if __name__ == '__main__':
    main()