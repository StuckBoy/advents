import re

def double_sequence(entry):
    return re.search(r'(..).*\1', entry)

def overlap(entry):
    return re.search(r'(.).\1', entry)

def check_criteria(entry):
    return double_sequence(entry) and overlap(entry)

if __name__ == '__main__':
    data = open('input.txt', 'r')
    inputs = data.readlines()
    nice_inputs = []
    naughty_inputs = []
    for value in inputs:
        if check_criteria(value.strip('\n')):
            nice_inputs.append(value)
        else:
            naughty_inputs.append(value)
    print("Nice: " + str(len(nice_inputs)))
    print("Naughty: " + str(len(naughty_inputs)))

