
""" Question 1 """

## Part A and B

filename = 'A_Journal_of_the_Plauge_Year.txt'

def filter_word(word):
    """ Remove trailing separation characters and convert to lower case. """
    return word.strip('.,!?;:)([]').lower()

word_occurence = dict()
N_words = 0

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:

            # -- Increase the number of total words by one
            N_words += 1

            # -- Remove special characters from the beginning and end of the word
            word = filter_word(word)

            # -- Increase the number of occurences of the word by one
            if word not in word_occurence:
                word_occurence[word] = 1
            else:
                word_occurence[word] += 1

print('Total number of words:', N_words)

## Part C

N_unique_words = len(word_occurence)
print('Total number of unique words:', N_unique_words)

## Part D

sorted_word_occurence = sorted(word_occurence.items(), key=lambda item: -item[1])
highest_word_occurence = [ sorted_word_occurence[idx] for idx in range(10) ]

print('\n word | occurences | probability')
print('-'*6 + '+' + '-'*12 + '+' + '-'*13)

for word, occurence in highest_word_occurence:
    probability = 100. * occurence / N_words
    print(f" {word:4s} | {occurence:10d} | {probability:10.1f}%")
