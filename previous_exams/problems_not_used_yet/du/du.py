import os

def directory_info(path):
    files = dict()
    for filename in os.listdir(path):
        files[filename] = os.path.getsize(path + '/' + filename)
    return files

def prefix(byte):
    if byte > 1024**3:
        suffix = 'GiB'
        value = f'{byte/1024**3:.2f}'
    elif byte > 1024**2:
        suffix = 'MiB'
        value = f'{byte/1024**2:.2f}'
    elif byte > 1024:
        suffix = 'KiB'
        value = f'{byte/1024:.2f}'
    else:
        return f'{byte}B'  # just show as integer

    value = value.rstrip('0').rstrip('.')
    return f'{value}{suffix}'

def show_directory_info(path, directory_info):
    total_size = sum(directory_info.values())
    print(f'{path}: {prefix(total_size)}')
    for filename, size in directory_info.items():
        print(f'    {filename}: {prefix(size)}')
    # Use these?
    #    "├──"
    #    "└──"

# Testing
directory = '..'
info = directory_info(directory)

print(prefix(1024))
print(prefix(10240))
print(prefix(200000))
print(prefix(1234567890))

show_directory_info(directory, info)
