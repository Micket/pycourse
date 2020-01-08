def read_paragraphs(filename):
    # See the textfile "input_example.txt" for how the input is formatted
    # LaTeX-style  paragraphs (empty lines define a new paragraph.
    # NOTE: This code is slightly more general than what is required on the actual exam example,
    # due to all paragraphs in the example always being on one line.
    # This was a mistake in input_example.txt (in the students favor) that was discovered to late.
    paragraphs = []
    partial = []
    with open(filename) as f:
        for line in f:
            if len(line) == 1:
                # Just a linebreak, so we finalize this partial paragraph and start a new.
                if partial:
                    # There may be multiple empty lines, so we check it we have something to add yet.
                    paragraphs.append(partial)
                    partial = []
            else:
                partial.extend(line.split())
    # File ended, but we might have a last paragraph not included in the list yet:
    if partial:
        paragraphs.append(partial)
    return paragraphs

def read_paragraphs_single_line(filename):
    # This trivial code would work on the exam for the given file:
    paragraphs = []
    with open(filename) as f:
        for line in f:
            if len(line) > 1:
                paragraphs.append(line.split())
    return paragraphs


def format_file_simple(paragraphs, output_filename, max_cols=80):
    with open(output_filename, 'w') as f:
        for paragraph in paragraphs:
            # New paragraph should be indented by 4 spaces:
            f.write(' '*4)
            char_count = 4

            for word in paragraph:
                n = len(word)
                if char_count + n <= max_cols:
                    # Word fits within line, write it:
                    char_count += n + 1
                    f.write(word + ' ')
                else:
                    # doesn't fit, print on the next line:
                    f.write('\n' + word + ' ')
                    char_count = n + 1
            f.write('\n')

#paragraphs = read_paragraphs('small_input.txt')
#print(paragraphs)

# this was the intended input example file
#paragraphs = read_paragraphs('intended_input_example.txt')
# but this also worked during the exam using the trivial code:
paragraphs = read_paragraphs_single_line('input_example.txt')
format_file_simple(paragraphs, 'student_example.txt')
