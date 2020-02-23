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
        return self.next_node
    def set_next(self):
        self.next_node = next_node
    def get_data(self):
        return self.data
    def set_data(self):
        self.data = data