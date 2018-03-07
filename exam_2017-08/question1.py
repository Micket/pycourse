def extract_mad_libs(filename):
    # This function could be very easily implemented using a regex, but this shows an alternative using str.find:
    placeholders = []
    with open(filename) as f:
        for line in f:
            for section in line.split('[')[1:]:
                placeholders.append(section.split(']')[0])
    return placeholders


def apply_mad_libs(input_filename, words, output_filename):
    with open(input_filename) as input_file, open(output_filename, 'w') as output_file:
        num = 0
        for line in input_file:
            sections = line.split('[')
            output_file.write(sections[0])
            for section in sections[1:]:
                placeholder, text = section.split(']')
                output_file.write(words[num])
                print('{} -> {}'.format(placeholder, words[num]))
                num += 1
                output_file.write(text)


filename = 'job_interview.txt'
words = extract_mad_libs(filename)
print(words)

from job_interview_words import *
apply_mad_libs(filename, job_interview_words, 'funny_' + filename)
