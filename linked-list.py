'''
OPERATIONS FOR OUR LINKED LIST:
1) Get Size
2) Find Data
3) Add Data
4) Remove Data
'''

# Let's get this bread ???? :)

class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node.data
    
    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next_node = next_node
    
class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0
   
    def get_size(self):
        return self.size
   
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
   
    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    
    def find(self, data):
        this_node = self.root

        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None
        
practiceList = LinkedList()
node1 = Node(1)
node2 = Node(2)

node1.set_next(node2)

print("NODE1 NEXT", node1.get_next())


print("[FOUND THE VALUE]:", practiceList.find(6))
print("[CURRENT SIZE]:", practiceList.get_size())
print("[REMOVED VALUE 13]:", practiceList.remove(13))
print("[SIZE AFTER VALUE REMOVAL]:", practiceList.get_size())
