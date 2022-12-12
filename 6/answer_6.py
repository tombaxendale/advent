f = open('6/input.txt', 'r')
input = f.read()
signal = list(input)

def unique_block_detector(message, marker_length):
    for i in range(marker_length - 1, len(message)):
        sample = message[i-marker_length + 1:i + 1] # slice last n characters
        sample_set = set(sample) # distinct values
        if len(sample_set) == marker_length:
            return i+1 # return breaks loop

answer_6a = unique_block_detector(signal, 4)
print(answer_6a)

answer_6b = unique_block_detector(signal, 14)
print(answer_6b)
