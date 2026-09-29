#IMPLEMENT A QUEUE USING TEH STACK

class MyQueue:

    def __init__(self):
        # Stack 1 is used to receive/store
        # all newly added elements.
        self.input_stack = []

        # Stack 2 is used when we need to
        # remove or see the front element.
        self.output_stack = []

    def push(self, x):
        # Add the new element into the input stack.
        self.input_stack.append(x)

    def pop(self):
        # If output stack is empty,
        # we need to transfer elements from
        # input stack to output stack.
        if not self.output_stack:

            # Move all elements from input_stack
            # to output_stack.
            #
            # This reverses their order.
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        # The top of output_stack is now
        # the FRONT of our queue.
        return self.output_stack.pop()

    def peek(self):
        # If output stack is empty,
        # transfer elements from input to output.
        if not self.output_stack:

            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        # The top of output_stack represents
        # the front element of the queue.
        return self.output_stack[-1]

    def empty(self):
        # Queue is empty only when BOTH stacks are empty.
        return not self.input_stack and not self.output_stack


# ==================================================
# TESTING IN VS CODE
# ==================================================

queue = MyQueue()

# Add elements to the queue
queue.push(10)
queue.push(20)
queue.push(30)

print("Input Stack:", queue.input_stack)
print("Output Stack:", queue.output_stack)

# Peek the front element
print("Front:", queue.peek())

# Remove the front element
print("Removed:", queue.pop())

# Peek again
print("Front:", queue.peek())

# Remove remaining elements
print("Removed:", queue.pop())
print("Removed:", queue.pop())

# Check whether queue is empty
print("Is Empty:", queue.empty())