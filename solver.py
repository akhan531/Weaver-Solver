import json
CACHE_FILE = "neighbor_dict.json"

with open(CACHE_FILE) as f:
    neighbor_dict = {k: set(v) for k, v in json.load(f).items()}



print("Start: ")       
start = input().upper()
print("End: ")  
end = input().upper()

print(start, end)

def h(word):
    diff = 0
    for w, e in zip(word,end):
        if w!=e:
            diff+=1
    return diff


import heapq

# A*
frontier = [(h(start), start, None)]
heapq.heapify(frontier)
visited = set()

while frontier:
    popped = heapq.heappop(frontier)
    f, curr, _ = popped
    if curr == end:
        break

    visited.add(curr)
    for neighbor in neighbor_dict[curr]:
        if neighbor not in visited:
            heapq.heappush(frontier, (f+1+h(neighbor)-h(curr), neighbor, popped))

# BFS           
# frontier = [(0, start, None)]
# heapq.heapify(frontier)
# visited = set()

# while frontier:
#     popped = heapq.heappop(frontier)
#     f, curr, _ = popped
#     if curr == end:
#         break
    
#     visited.add(curr)
#     for neighbor in neighbor_dict[curr]:
#         if neighbor not in visited:
#             heapq.heappush(frontier, (f+1, neighbor, popped))



path = []

while popped:
    _, curr, prev = popped
    path.append(curr)
    popped = prev

path.reverse()


print(path)