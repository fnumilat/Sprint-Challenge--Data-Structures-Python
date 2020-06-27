from db_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if the storage is full
        # if not add the new item to the head
        if len(self.storage) < self.capacity:
            self.storage.add_to_head(item)
            #if the length of storage is only 1 then point it to the current
            if len(self.storage) == 1:
                self.current = self.storage.head
            return
        # check if the storage and the capacity are the same
        # and if there are other items in the storage then point the previous to the current item
        # and if there is no other item then make the current item the tail
        if len(self.storage) == self.capacity:
            self.current.value = item
            if self.current.prev is not None:
                self.current = self.current.prev
            else:
                self.current = self.storage.tail
        


    def get(self):
        ring_buffer_array = []
        cur = self.storage.tail

        # loop through the storage and add the current item to the list and return the list
        for _ in range(0, len(self.storage)):
            ring_buffer_array.append(cur.value)
            cur = cur.prev
            
        return ring_buffer_array

    
