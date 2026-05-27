import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    l = []
    for n in nums:
        pair = (-n, n)
        heapq.heappush(l, pair)
    
    result = []
    while l:
        pair = heapq.heappop(l)
        result.append(pair[1])
    result.sort(reverse = True)
    return result


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
