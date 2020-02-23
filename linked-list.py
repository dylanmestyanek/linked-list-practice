'''
OPERATIONS FOR OUR LINKED LIST:
1) Get Size
2) Find Data
3) Add Data
4) Remove Data
'''

# Let's get this bread ???? :)

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next
    def get_next(self):
        return self.next_node