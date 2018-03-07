# Part A

filename = 'data.txt'
data = []

with open(filename, 'r') as fil:
    for line in fil:
        if not line.strip():
            continue
        typ, name, age = (s.strip() for s in line.split(','))
        item = {'Name': name, 'Age': age, 'Type': typ}        
        data.append(item)
for item in data:
    print(item)

# Part B
class ExtractNames:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        class NameIterator:
            def __init__(self, it):
                self.it = it

            def __next__(self):
                return next(self.it)['Name']

        return NameIterator(iter(self.data))


print(list(ExtractNames(data)))
