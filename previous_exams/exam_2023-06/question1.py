def read_paragraphs(filename: str) -> list[list]:
    # LaTeX-style  paragraphs (empty lines define a new paragraph.
    paragraphs = []
    partial = []
    with open(filename) as f:
        for line in f:
            if len(line.strip()) < 1:
                # Empty line (besides possible whitespace), so we finalize this partial paragraph and start a new.
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


def format_file(paragraphs: list[list], output_filename: str, max_cols: int=80) -> None:
    with open(output_filename, 'w') as f:
        for paragraph in paragraphs:
            # New paragraph should be indented by 4 spaces:
            f.write(' '*4)
            char_count = 4

            need_space = False  # This is a bit overkill, but can help is avoid unncessary trailing spaces.
            for word in paragraph:
                n = len(word)
                # Word doesn't fit in remaining space, restart on new line
                if char_count + n + need_space > max_cols:
                    f.write('\n')
                    char_count = 0
                    need_space = False

                if need_space:
                    f.write(' ')
                    char_count += 1

                f.write(word)
                char_count += n
                need_space = True

            f.write('\n')

paragraphs = read_paragraphs('small_input.txt')
print(paragraphs)

paragraphs = read_paragraphs('example_input.txt')
format_file(paragraphs, 'example_output.txt')
