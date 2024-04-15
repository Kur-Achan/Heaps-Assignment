import heapq

heap = [20,36,44,56]

heapq.heapify(heap)
heapq. heappush(heap, 25)
heapq. heappush(heap,12)
heapq.heappush(heap,4)

print (heap)

heapq.heappush(heap,24)
print(heap)

heapq.heappop(heap)
print(heap)


smallestElement = heapq.nsmallest(2,heap)
print(smallestElement)

minElement = heapq.heappop(heap)
print(heap)
largestElement = heapq.nlargest(1,heap)
print(largestElement)
smallestElement = heapq.nsmallest(2,heap)
print(smallestElement)
minElement = heapq.heappop(heap)
print(minElement)



