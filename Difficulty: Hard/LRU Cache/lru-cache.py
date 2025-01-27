#User function Template for python3
from collections import deque
# design the class in the most optimal way

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Dictionary to store key-value pairs
        self.cache = {}

        # Deque to maintain the order of keys
        self.order = deque()

    def get(self, key: int) -> int:
        if key in self.cache:

            # Move the accessed key to 
            # the front of the deque
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.cache:

            # Update the value and move
            # the key to the front
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:

                # Remove the least recently used item
                lru_key = self.order.pop()
                del self.cache[lru_key]

            # Add the new key-value pair
            self.cache[key] = value
            self.order.appendleft(key)






#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends