

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    # # get the value of current node
    # def get_value(self):
    #     return self.value

    # # get the key of current node
    # def get_key(self):
    #     return self.key

    # # get the ref to the next node in the chain
    # def get_next(self):
    #     return self.next_node

    # # set the ref to the next node in the chain
    # def set_next(self, new_next):
    #     self.next_node = new_next


# class LinkedList:
#     def __init__(self):
#         # set initial ref to head
#         self.head = None
#         # set initial rer to tail
#         self.tail = None

#     def add_to_tail(self, value):
#         # wrap the val inside a node
#         new_node = Node(value, None)
#         # 1. the lists empty
#         if not self.head:
#             # check if no head
#             # set head and tail to new node
#             self.head = new_node
#             self.tail = new_node
#         # 2. if not empty
#         else:
#             # add a new node to the tail
#             self.tail.set_next(new_node)
#             # set tails next ref to our new node
#             self.tail = new_node

#     def remove_head(self):
#         # return None if there is no head (empty List)
#         if not self.head:
#             return None
#         # if single node list
#         if not self.head.get_next():
#             # get ref to head
#             head = self.head
#             # del head from list
#             self.head = None
#             # del tail from list
#             self.tail = None
#             # return the head to the caller
#             return head.get_value()

#         # otherwise store value
#         value = self.head.get_value()
#         # set heads ref to current heads next node in the list
#         self.head = self.head.get_next()
#         return value

#     def contains(self, value):
#         if not self.head:
#             return False

#         # get ref to node we are currently at; update as we traverse list
#         current = self.head

#         # check to see if valid node
#         while current:
#             # if current node matches return true
#             if current.get_value() == value:
#                 return True

#             # update our current node to the next node in the list
#             current = current.get_next()
#         # if we are here. then the target value is not in the list
#         return False

    # def contains_key(self, key):
    #     if not self.head:
    #         return False

    #     # get ref to node we are currently at; update as we traverse list
    #     current = self.head

    #     # check to see if valid node
    #     while current:
    #         # if current node matches return true
    #         if current.get_key() == key:
    #             return True

    #         # update our current node to the next node in the list
    #         current = current.get_next()
    #     # if we are here. then the target value is not in the list
    #     return False


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.original_capacity = capacity
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity
        # count to include ll items and array items
        self.count = 0



# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return hash % max



# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    lp = hash_table.storage[index]
    if lp is None:
        lp = LinkedPair(key, value)
        hash_table.storage[index] = lp
        hash_table.count += 1
    else:
        while True:
            if lp.key == key:
                lp.value = value
                return
            if lp.next is None:
                break
            lp = lp.next
        lp.next = LinkedPair(key, value)


    # otherwise setup a new linked pair and remember to set up the next pointer 
    # to the item at the storage index before adding the new pair

    

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    lp = hash_table.storage[index]
    if lp is None:
        print(f"WARNING: key not found")

    prev_lp = None
    while lp.key != key and lp.next is not None:
        prev_lp = lp
        lp = lp.next

    if lp.key == key:
        if lp.next is not None:
            prev_lp.next = lp.next
        else:
            if prev_lp is None:
                # there was only one item here and we're removing it
                hash_table.storage[index] = None
                hash_table.count -= 1
            else:
                prev_lp.next = None




# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    lp = hash_table.storage[index]
    if lp is None:
        return None

    while lp.key != key and lp.next is not None:
        lp = lp.next

    if lp.key == key:
        return lp.value
    else:
        return None



# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    load_factor = hash_table.count / hash_table.capacity
    new_hash_table = hash_table
    needs_resize = False

    # if load limits exceeded,
    # make a new hash table with half the capacity and
    # insert each element from the old one
    if load_factor > 0.7:
        new_hash_table = HashTable(hash_table.capacity * 2)
        new_hash_table.original_capacity = hash_table.capacity
        needs_resize = True
    elif (hash_table.original_capacity != hash_table.capacity
    and load_factor < 0.2):
        new_hash_table = HashTable(hash_table.capacity // 2)
        needs_resize = True

    if needs_resize:
        for i in range(hash_table.count):
            lp = hash_table.storage[i]
            while True:
                if lp is None:
                    break
                hash_table_insert(new_hash_table, lp.key, lp.value)
                lp = lp.next

    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
