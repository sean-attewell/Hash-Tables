# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):

        # max length of array
        self.capacity = capacity
        # occupied length of array
        self.count = 0
        # underlying data sructure
        self.elements = [None] * capacity


# Double the size of the given array
def resize_array(arr):
    # Your code here

    # set new capacity to double
    new_capacity = arr.capacity * 2

    # create the new elements storage unit
    new_elements = [None] * new_capacity

    # copy over the elements
    for i in range(arr.count):
        new_elements[i] = arr.elements[i]

    # set the new elements and capacity to the current array instance
    arr.elements = new_elements
    arr.capacity = new_capacity


# Return an element of a given array at a given index
def array_read(arr, index):
    # Throw an error if array is out of the current count
    if index >= arr.count:
        print("ERROR: element " + str(index) + " is out of range.")
        return None

    return arr.elements[index]


# Insert an element in a given array at a given index
def array_insert(arr, element, index):
    # Throw an error if array is out of the current count
    if index > arr.count:
        print("ERROR: element " + str(index) + " is out of range")
        return None
    # Resize the array if the number of elements is over capacity
    if arr.capacity <= arr.count:
        resize_array(arr)
    # Move the elements to create a space at 'index'
    # Think about where to start!
    for i in range(arr.count, index, - 1):
        arr.elements[i] = arr.elements[i - 1]

    # Add the new element to the array and update the count
    arr.elements[index] = element
    arr.count += 1


# Add an element to the end of the given array
def array_append(arr, element):

    # Hint, this can be done with one line of code
    # (Without using a built in function)
    array_insert(arr, element, arr.count)


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(arr, element):
    # set a bool to check if removed
    removed = False
    # loop over the elements
    for i in range(arr.count):
        # if the element is removed
        if removed:
            arr.elements[i - 1] = arr.elements[i]
        # otherwise set removed
        elif arr.elements[i] == element:
            removed = True

    # if items set to removed
    if removed:
        # decrement count
        arr.count -= 1
        # set at the elements at count to none
        arr.elements[arr.count] = None
    # otherwise throw the error
    else:
        print("ERROR: " + str(element) + " not found")


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop(arr, index):
    # Throw an error if array is out of the current count
    if index > arr.count:
        print("ERROR: " + str(index) + " is out of range")
        return None

    # store the return value foer later
    return_value = arr.elements[index]

    # shift the elements
    for i in range(index + 1, arr.count, 1):
        arr.elements[i - 1] = arr.elements[i]

    # decrement count
    arr.count -= 1

    # set end of array to None
    arr.elements[arr.count] = None

    # return the stored return value
    return return_value


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
arr = array(1)

array_insert(arr, "STRING1", 0)
array_print(arr)
array_pop(arr, 0)
array_print(arr)
array_insert(arr, "STRING1", 0)
array_print(arr)
array_append(arr, "STRING4")
array_print(arr)
array_insert(arr, "STRING2", 1)
array_print(arr)
array_insert(arr, "STRING3", 2)
array_print(arr)
