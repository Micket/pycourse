import os

def read_directory(path):
    files = dict()
    for filename in os.listdir(path):
        files[filename] = os.path.getsize(os.path.join(path, filename))
    return files

def format_bytes(byte):
    if byte >= 1024**3:
        suffix = 'GiB'
        value = byte/1024**3
    elif byte >= 1024**2:
        suffix = 'MiB'
        value = byte/1024**2
    elif byte >= 1024:
        suffix = 'KiB'
        value = byte/1024
    else:
        return f'{byte}B'  # just show as integer

    # Many ways to achieve this
    if value.is_integer():
        return f'{value:.0f}{suffix}'
    else:
        return f'{value:.2f}{suffix}'

def show_directory_info(path, directory_info):
    total_size = sum(directory_info.values())
    print(f'{path}: {format_bytes(total_size)}')
    
    data = sorted(directory_info.items(), key=lambda v: v[1], reverse=True)
    for i, (filename, size) in enumerate(data):
        # Exam requested pipes, plus and dashes. but we can also use unicode to make it really fancy
        prefix = "└──" if i == len(data)-1 else "├──"
        print(f'{prefix} {filename}: {format_bytes(size)}')

# Testing
path = 'example_directory'
dinfo = read_directory(path)
print(dinfo)

print(format_bytes(42))
print(format_bytes(1024))
print(format_bytes(12288))
print(format_bytes(200000))
print(format_bytes(1234567890))
print()

show_directory_info(path, dinfo)
