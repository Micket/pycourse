# Part A
def camel_caser(name):
    # Converts underscore to camel case, e.g. "my_class_name" to "MyClassName"
    return ''.join(x.capitalize() for x in name.split('_'))

x = camel_caser('my_class_name')
print(x)


# Part B: Replace the badly named classes:
inputfile = 'student_code.py'
outputfile = 'readable_code.py'

with open(outputfile, 'w') as fout:
    with open(inputfile, 'r') as fin:
        for line in fin:
            if line.startswith('class'):
                w = line.split(' ')
                w[1] = camel_caser(w[1])
                new_line = ' '.join(w)
                fout.write(new_line)
            else:
                fout.write(line)
