class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None




class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left
    
    def insert(self,node):
        p=self.right.prev
        p.next=node
        node.prev=p
        node.next=self.right
        self.right.prev=node

    def remove(self,node):
        p=node.prev
        p.next=node.next
        node.next.prev=p

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            del self.cache[key]
        new_node=Node(key,value)
        self.cache[key]=new_node
        self.insert(new_node)

        if len(self.cache)>self.capacity:
            n=self.left.next
            self.left.next=n.next
            n.next.prev=self.left
            del self.cache[n.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)