#!/usr/bin/env python3

def return_evens(num_list):
    # Initialize an empty list to store even numbers
    even_numbers = []

    # Iterate through each number in num_list
    for num in num_list:
        # Check if the number is even
        if num % 2 == 0:
            even_numbers.append(num)  # Add even number to the list

    return even_numbers

def make_exclamation(sentence_list):
    # Initialize an empty list to store sentences with exclamation marks
    exclamations = []

    # Iterate through each sentence in sentence_list
    for sentence in sentence_list:
        # Add an exclamation mark at the end of the sentence
        exclamations.append(sentence + "!")

    return exclamations

# Test cases
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(return_evens(num_list))  # Output: [0, 2, 4, 6, 8]

sentence_list = ["I like computers", "I require coffee", "Live long and prosper"]
print(make_exclamation(sentence_list))
# Output: ['I like computers!', 'I require coffee!', 'Live long and prosper!']
