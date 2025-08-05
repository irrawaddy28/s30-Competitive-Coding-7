
import heapq

def minMeetingRooms(intervals):
    '''
    253 Meeting Rooms II
    https://leetcode.com/problems/meeting-rooms-ii/

    N = no. of intervals, K = min number of meeting rooms
    (worst case K = N, all meetings overlap)
    Avg:
        Time: O(N log N + N log K) = O(N log NK), Space: O(K)
    Worst (K=N):
        Time: O(N log N*2) = O(2N log N) = O(N log N), Space: O(N)
    '''
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0]) # O(N log N)
    heap = [intervals[0][1]] # end time of first meeting

    #num_rooms = 1 # = len(heap)
    for ival in intervals[1:]:
        st_curr, end_curr = ival # interval of curr meeting
        end_prev = heap[0] # meeting with the earliest end time in heap

        # if start(curr meeting) < end(prev meeting) -> meeting overlap
        if st_curr < end_prev:
            heapq.heappush(heap, end_curr) # size of heap increases by 1 (push)
        else: # meetings do not overlap
            heapq.heappushpop(heap, end_curr) # size of heap doesnt change (push+pop)

        #num_rooms = max(num_rooms, len(heap))
    return len(heap)
    # Note: Even if we compute num_rooms in the for loop, we still end up with  len(heap) at the end of the loop. Note that the heap size can only increase but cannot decrease. When a new meeting overlaps with another meeting, heap size increases by 1. When a new meeting does not overlap, heap size doesn't change.


def run_minMeetingRooms():
    tests = [([[0,30],[5,10],[15,20]], 2),
             ([[0,30],[9,20],[5,10]], 3),
             ([[7,10],[2,4]], 1),
             ([[0,30],[5,10],[15,20],[25,35]], 2),
             ([[0,30],[5,10],[15,20],[25,35],[28,30]], 3),
    ]
    for test in tests:
        intervals, ans = test[0], test[1]
        result = minMeetingRooms(intervals)
        success = (ans == result)
        print(f"\nIntervals = {intervals}")
        print(f"Min. no. of rooms = {result}")
        print(f"Pass: {success}")
        if not success:
            return

run_minMeetingRooms()