
# '''
# Basic hash table key/value pair
# '''


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):  # were also given second parameter 'max'
    hash = 5381
    for c in string:
        hash = (hash * 33) + ord(c)
    # modulo finds the remainder of division of one number by another
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''

# index = hash_function(Key) % array.length
# array [index] = value
def hash_table_insert(hash_table, key, value):
    # find index by hashing the key
    index = hash(key, hash_table.capacity)
    # instantiate Pair class
    p = Pair(key, value)

    # see if there is a value stored at that index
    if hash_table.storage[index] != None:
        print("WARNING: Inserting with this key has overwritten an existing insert")
    # save value to index
    hash_table.storage[index] = p.value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    # find index by hashing the key
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] == None:
        print("No value assigned to that key")
    else:
        hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''

def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] == None:
        return None
    else:
        return hash_table.storage[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
