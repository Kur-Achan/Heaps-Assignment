import heapq

heap =[]

heapq.heappush(heap,40)
heapq. heappush(heap, 25)
heapq. heappush(heap,12)
heapq.heappush(heap,4)

print (heap)





heap = [40,25,12,4]
largest = heapq.heappop(heap)

print(largest)
print(heap)