import os

def directory_info(path):
    files = dict()
    for filename in os.listdir(path):
        files[filename] = os.path.getsize(path + '/' + filename)
    return files

def format_bytes(byte):
    if byte >= 1024**3:
        suffix = 'GiB'
        value = f'{byte/1024**3:.2f}'
    elif byte >= 1024**2:
        suffix = 'MiB'
        value = f'{byte/1024**2:.2f}'
    elif byte >= 1024:
        suffix = 'KiB'
        value = f'{byte/1024:.2f}'
    else:
        return f'{byte}B'  # just show as integer

    value = value.rstrip('0').rstrip('.')
    return f'{value}{suffix}'

def show_directory_info(path, directory_info):
    total_size = sum(directory_info.values())
    print(f'{path}: {format_bytes(total_size)}')
    
    data = sorted(directory_info.items(), key=lambda v: v[1], reverse=True)
    for i, (filename, size) in enumerate(data):
        prefix = "└──" if i == len(data)-1 else "├──"
        print(f'{prefix} {filename}: {format_bytes(size)}')

# Testing
directory = 'example_directory'
info = directory_info(directory)

print(format_bytes(42))
print(format_bytes(1024))
print(format_bytes(12288))
print(format_bytes(200000))
print(format_bytes(1234567890))
print()

show_directory_info(directory, info)
