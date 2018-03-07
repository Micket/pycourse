def read_spellcorrections(filename):
    corrections = dict()
    with open(filename) as f:
        for line in f:
            correct, typos = line.split(':')
            typos = typos.strip('{} \n')
            for typo in typos.split(','):
                 corrections[typo.strip()] = correct.strip()
    return corrections

def split_punctuation(text):
    word = text.strip('.,:!?')
    punc = text[len(word):]
    return word, punc

def correct_line(line, corrections):
    # Support function for "correct_file" which works on a single line.
    new_words = []
    words = line.split()
    for word in words:
        word, punc = split_punctuation(word)
        # Store whether or not the word is capitalized
        capitalized = word[0].isupper()
        # Correct the word (if it's mistyped)
        word = word.lower()
        if word in corrections:
            word = corrections[word]
        # Re-capitalize corrected words
        if capitalized:
            word = word.capitalize()
        new_words.append(word + punc)
    return ' '.join(new_words) + '\n'

def correct_file(input_filename, output_filename, corrector):
    with open(input_filename) as input:
        with open(output_filename, 'w') as output:
            for line in input:
                new_line = correct_line(line, corrector)
                output.write(new_line)

# Testing the code:
# A
corr = read_spellcorrections('spelling_corrections.txt')
print(corr['nieghbour'])

# B
print(split_punctuation('Tiger!'))
print(split_punctuation('cat'))
print(split_punctuation('sigh...'))

# C
print(correct_line('Have you seen my neighbourh?', corr))
print(correct_line('Wantid, daed or alive.', corr))

# The real deal:
correct_file('text_with_typos.txt', 'corrected.txt', corr)
