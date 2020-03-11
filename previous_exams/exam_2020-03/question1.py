
""" Question 1 """


# Part A


def read_degree_data(filename, encoding='ISO-8859-1'):
    
    with open(filename, 'r', encoding=encoding) as file:

        title = file.readline()
        _ = file.readline()
        header = file.readline().strip().replace('"','').split(',')
        header, years = header[:4], header[4:]

        degrees = {}

        for line in file:
            row = line.strip().replace('"','').split(',')

            school, degree, gender, age = row[:4]
            degrees_per_year = [ int(x) for x in row[4:] ]

            key = (school, degree, gender, age)
            degrees[key] = degrees_per_year

    return degrees, years


# Part B


def accumulate_degrees_per_school(degrees):

    degrees_per_school = {}

    for (school, degree, gender, age), degrees_per_year in degrees.items():
        if school in degrees_per_school:
            degrees_per_school[school] = [ x + y for x, y in zip(degrees_per_year, degrees_per_school[school]) ]
        else:
            degrees_per_school[school] = degrees_per_year

    return degrees_per_school

        
# Part C


def print_table(years, degrees_per_school):

    school_labels = [ ('CTH' if 'Chalmers' in school else 'KTH') for school in degrees_per_school.keys() ]
    
    print('{:7s} | {:>5s} {:>5s}'.format('Year', *school_labels))
    print('-'*24)
    for item in zip(years, *degrees_per_school.values()):
        year, numbers = item[0], item[1:]
        print('{:>7s} | {:5d} {:5d}'.format(year, *numbers))


# Final usage of all functions


if __name__ == '__main__':

    degrees, years = read_degree_data(filename='scb_degrees_per_year.csv')

    degrees_per_school = accumulate_degrees_per_school(degrees)

    print_table(years, degrees_per_school)

