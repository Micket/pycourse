import abc
import os
import random

# Intentionally avoiding __iter__ here as we used it in q3 already, to mix things up.

class Dataset(abc.ABC):
    def __init__(self, name):
        self.name = name

    def rand(self):
        return self[random.randrange(0,len(self))]

    @abc.abstractmethod
    def __getitem__(self):
        pass

    @abc.abstractmethod
    def __len__(self):
        pass


class ListDataset(Dataset):
    def __init__(self, name, data):
        super().__init__(name)
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        return f'ListDataset({self.name})'


class DirectoryDataset(Dataset):
    def __init__(self, path):
        super().__init__(path.split('/')[-1])
        self.path = path

    def __len__(self):
        return len(os.listdir(self.path))

    def __getitem__(self, item):
        filename = os.listdir(self.path)[item]
        with open(os.path.join(self.path, filename)) as file:
            return file.read()

    def __repr__(self):
        return f'DirectoryDataset({self.name})'


class SubsetDataset(Dataset):
    def __init__(self, dataset, subrange):
        super().__init__(dataset.name)
        self.subrange = subrange
        self.dataset = dataset

    def __len__(self):
        return len(self.subrange)
    
    def __getitem__(self, item):
        return self.dataset[self.subrange[item]]

    def __repr__(self):
        return f'SubsetDataset({self.dataset}, {self.subrange})'


class RandomDataset(Dataset):
    def __getitem__(self, _):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(10))

    def __len__(self):
        return 1

    def __repr__(self):
        return f'RandomDataset({self.name})'




# Test

a = ListDataset('test strings', ["some", "simple", "example data", "here"])
b = DirectoryDataset('example/poems')
c = DirectoryDataset('example/limericks')
d = SubsetDataset(c, range(1,7,2))
e = RandomDataset('testing')

assert a[1] == "simple"
assert b[3].startswith("There once was a text editor called PyCharm")
assert c.name == "limericks"
assert d.name == "limericks"
assert d[1] == 
assert len(c) == 6  # 6 example limericks
assert len(d) == 2
assert e.rand() == 10  # should be a random 10 character string

print(a.rand())
print(b.rand())
print(d.rand())
