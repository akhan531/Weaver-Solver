import json
import os



CACHE_FILE = "neighbor_dict.json"


length = 4

with open("words.txt") as f:
    words = [line.strip() for line in f if line.strip()]
n = len(words)

def areNeighbors(word1, word2):
    diff = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            diff+=1
            if diff==2:
                return False
    return diff == 1

neighbor_dict = {word: set() for word in words}
for i in range(n):
    for j in range(i+1,n):
        if areNeighbors(words[i], words[j]):
            neighbor_dict[words[i]].add(words[j])
            neighbor_dict[words[j]].add(words[i])
with open(CACHE_FILE, "w") as f:
    json.dump({k: list(v) for k, v in neighbor_dict.items()}, f)