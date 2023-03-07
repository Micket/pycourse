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
    """ Dataset simply stored in list """
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
    # a bit boring maybe?
    def __len__(self):
        return len(os.listdir(self.name))

    def __getitem__(self, item):
        filename = os.listdir(self.name)[item]
        with open(os.path.join(self.name, filename)) as file:
            return filename.read()

    def __repr__(self):
        return f'DirectoryDataset({self.name})'


class H5Dataset(Dataset):
    def __init__(self, archivepath):
        super().__init__(archivepath.split('/')[-1])
        self.archive = h5py.File(archivepath, 'r')

    def __getitem__(self, item):
        return self.archive[str(item)][()]

    def __repr__(self):
        return f'H5Dataset({self.name})'


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



# Test

a = ListDataset('test strings', ["some", "simple", "example data", "here"])
b = DirectoryDataset('example/limericks')
c = DirectoryDataset('example/poems')
d = SubsetDataset(c, range(1,3))

#assert len(c) == 6
#assert len(d) == 2

print(d.rand())
