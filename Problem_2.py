'''
378 Kth Smallest Element in Sorted Matrix

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix. Note that it is the kth smallest element in the sorted order, not the kth distinct element. You must find a solution with a memory complexity better than O(n^2).



Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?

Solution:
1. Min heap:
Time: O(N*N log K), Space: O(K)

2. Binary search:
Time: O(NlogN * logR), Space: O(1), R = max(matrix) - min(matrix)
'''
import heapq

def kthSmallest_minheap(matrix, k):
    '''
    378 Kth smallest element in matrix
    https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

    Max heap of size k
    Time: O(N*N log K), Space: O(K)
    '''
    if not matrix:
        return float('-inf')
    N = len(matrix)
    heap = []
    for i in range(N):
        for j in range(N):
            num = -matrix[i][j]
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
    return -heap[0]

def kthSmallest_binarysearch(matrix, k):
    '''
    378 Kth smallest element in matrix
    https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

    Binary search
    Time: O(NlogN * logR), Space: O(1), R = max(matrix) - min(matrix)
    '''
    def countLE(mid):
        ''' Time: O(N^2), Space: O(1)'''
        count = 0
        for i in range(n):
            j = n-1
            while j>=0:
                if matrix[i][j] > mid:
                    j -= 1
                else: # matrix[i][j] <= mid:
                    break
            count = count + j + 1
        return count

    def get_max_lb(arr, s, e, target):
        ''' Time: O(log N), Space: O(1)'''
        while s <= e:
            m = s + (e-s)//2
            if arr[m] <= target:
                s = m + 1
            else:
                e = m - 1
        return s-1

    def countLE_binarysearch(mid):
        ''' Time: O(N log N), Space: O(1)'''
        count = 0
        for i in range(n): # O(N)
            j = get_max_lb(matrix[i], 0, n-1, mid) # O (log N)
            count = count + j + 1
        return count


    n = len(matrix)
    low = matrix[0][0]
    high = matrix[-1][-1]

    while low < high: # O(log(max matrix - min matrix)) = O(log R)
        mid = low + (high - low)//2 #s + (e-s)//2
        # count = countLE(mid) # O(N^2)
        count = countLE_binarysearch(mid) # O(N log N)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low

def run_kthSmallest():
    tests = [([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
             ([[-5]], 1, -5),
    ]
    for test in tests:
        matrix, k, ans = test[0], test[1], test[2]
        for method in ['min-heap', 'binary-search']:
            if method == 'min-heap':
                result = kthSmallest_minheap(matrix, k)
            elif method == 'binary-search':
                result = kthSmallest_binarysearch(matrix, k)
            success = (ans == result)
            print(f"\nMatrix = {matrix}")
            print(f"{method}: {k}th smallest = {result}")
            print(f"Pass: {success}")
            if not success:
                return

run_kthSmallest()