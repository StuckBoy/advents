import re

def valid_vowel_count(entry):
    # >= 3 vowels
    # return len(re.findall(r'[aeiou]+', entry)) >= 3
    return re.search(r'([aeiou].*){3,}', entry)

def doubles_present(entry):
    # Needs a double 'zz', 'cc', 'dd'
    return re.search(r'(.)\1' , entry)

def contains_illegal_pairs(entry):
    # *Does not* contain 'ab', 'cd', 'pq', or 'xy'
    return re.search(r'(ab|cd|pq|xy)', entry)

def check_criteria(entry):
    return valid_vowel_count(entry) and doubles_present(entry) and not contains_illegal_pairs(entry)

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

