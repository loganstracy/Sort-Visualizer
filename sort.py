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
    
    def insertion_sort(self):
        buffer = self.elements
        self.add_snapshot(buffer)
        for i in range(1, len(buffer)):
            key_item = buffer[i]

            j = i - 1

            while j >= 0 and buffer[j] > key_item:
                buffer[j + 1] = buffer[j]
                j -= 1
            
            buffer[j + 1] = key_item
            self.add_snapshot(buffer)


def quick_sort(elements):
    if len(elements) < 2:
        return elements
    
    low, same, high = [], [], []

    pivot = elements[randint(0, len(elements) - 1)]

    for item in elements:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    
    return quick_sort(low) + same + quick_sort(high)