class Logger:

    def __init__(self):
        # Container which contains the latest timestamp of each unique message
        self.container = {}

    def shouldPrintMessage(self, timestamp, message):
        # Getting the valid timestamp of the input message
        time = self.container.get(message, 0)
        # If the message comes before its assigned time, return False
        if time > timestamp:
            return False
        # If the message comes after its assigned time, update its time and return True
        self.container[message] = timestamp + 10
        return True


# Input stream given in the question
input_stream = [[1, 'foo'], [2, 'bar'], [3, 'foo'], [8, 'bar'], [10, 'foo'], [11, 'foo']]

# Output of the program will be stored in this list
output = []

# Creating an object of class Logger
logger = Logger()

for index in input_stream:
    output.append(logger.shouldPrintMessage(index[0], index[1]))

print("Output of the following program is:")
print(output)
