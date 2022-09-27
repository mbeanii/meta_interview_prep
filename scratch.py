def swap_pointers():
    global enqueue_pointer
    global dequeue_pointer

    temp = enqueue_pointer
    enqueue_pointer = dequeue_pointer
    dequeue_pointer = temp


stack_1 = []
stack_2 = []

enqueue_pointer = stack_1
dequeue_pointer = stack_2

enqueue_pointer.append("value")

print(stack_1)

swap_pointers()

enqueue_pointer.append("different_value")

print(stack_1)
print(stack_2)

print(len([4]))