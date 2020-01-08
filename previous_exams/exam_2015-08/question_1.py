__author__ = 'Kristoffer'

def luminance(R, G, B):
    return round(0.2126 * R + 0.7152 * G + 0.0722 * B)

def read_ppm(filename):
    with open(filename) as f:
        data = []
        for line in f:
            if line.startswith("#"):  # Ignore comments
                continue
            for word in line.strip().split():
                data.append(int(word))

    size_x = data[0]
    size_y = data[1]
    max_val = data[2]
    data = data[3:]
    return size_x, size_y, max_val, data

def write_pgm(filename, data, max_val, size_x, size_y):
    with open(filename, "w") as f:
        f.write("P2\n")
        f.write("# Greyscale version\n")
        f.write(str(size_x) + " " + str(size_y) + "\n")
        f.write(str(max_val) + "\n")
        for i, illum in enumerate(data):
            f.write(str(illum) + "\n")

def ppm2pgm(filename):
    size_x, size_y, max_val, data = read_ppm(filename)

    grays = []
    n_pixels = size_x * size_y
    for i in range(0, 3 * n_pixels, 3):
        # offsetting for sizes
        R = data[i]
        G = data[i + 1]
        B = data[i + 2]
        grays.append(luminance(R, G, B))

    write_pgm(filename[:-4] + ".pgm", grays, max_val, size_x, size_y)

ppm2pgm("file.ppm")
