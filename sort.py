from random import randint, shuffle

class SortContainer():
    def __init__(self, size=300, type='insertion'):
        self.size = size
        self.elements = self.new_elements()
        self.snapshot = []
        self.sort_type = type
        self.change_sort(self.sort_type)
    
    def new_elements(self):
        e = [x+1 for x in range(self.size)]
        shuffle(e)
        return e

    def shuffle_elements(self):
        shuffle(self.elements)
    
    def add_snapshot(self, custom=None):
        if custom == None:
            self.snapshot.append(self.elements[:])
        else:
            self.snapshot.append(custom[:])
    
    def clear_snapshot(self):
        self.snapshot = []
        self.snapshot.append(self.elements[:])
    
    def get_snapshot(self, index):
        return self.snapshot[index]
    
    def change_sort(self, type):
        self.clear_snapshot()
        self.sort_type == type

        if self.sort_type == 'insertion':
            self.insertion_sort()
        elif self.sort_type == 'heap':
            self.heap_sort()
    
    def insertion_sort(self):
        buffer = self.elements
        self.add_snapshot(buffer[:])
        for i in range(1, len(buffer)):
            key_item = buffer[i]

            j = i - 1

            while j >= 0 and buffer[j] > key_item:
                buffer[j + 1] = buffer[j]
                j -= 1
            
            buffer[j + 1] = key_item
            self.add_snapshot(buffer)

    def heapify(self, buffer, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * 1 + 2

        if l < n and buffer[i] < buffer[l]:
            largest = l
        if r < n and buffer[largest] < buffer[r]:
            largest = r
        if largest != i:
            buffer[i], buffer[largest] = buffer[largest], buffer[i]
            self.add_snapshot(buffer[:])
            self.heapify(buffer, i, 0)
        self.add_snapshot(buffer[:])

    def heap_sort(self):
        buffer = self.elements
        self.add_snapshot(buffer[:])
        n = len(buffer)
        
        for i in range(n//2, -1, -1):
            self.heapify(buffer, n, i)
        for i in range(n-1, 0, -1):
            buffer[i], buffer[0] = buffer[0], buffer[i]
            self.add_snapshot(buffer[:])
            self.heapify(buffer, i, 0)
        self.elements = buffer