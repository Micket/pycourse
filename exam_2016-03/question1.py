# Part A
def extract_bold(text):
    bold = list()
    for x in text.split('[b]')[1:]: # Drop the first part
        bold_segment = x.split('[/b]')[0]
        # Bonus: Lets also strip possible extra cruft like punctuation etc, and switch newlines to spaces.
        # Might as well make them lower case here as well (we could do this later, either way is fine)
        bold.append( bold_segment.replace('\n', ' ').strip(' .,').lower() )
    return bold

# Test
x = extract_bold('[i]Text[/i] with [b]bold text[/b] some [b]places[/b]')
print('Part A test:', x)


# Part B
from os import listdir

# path = 'C:\\Some\\Path\\bbcode\\'  # If you need a fixed path
path = 'bbcode/'  # Linux/OSX paths have / instead of \
segments = set()
for f in listdir(path):
    with open(path + f) as fid:
        segments.update(extract_bold(fid.read()))

with open('output.txt', 'w') as fid:
    for s in segments:
        fid.write(s + "\n")
        print(s)