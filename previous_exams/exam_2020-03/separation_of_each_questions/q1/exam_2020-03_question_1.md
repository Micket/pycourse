---
header-includes:
        - \usepackage[left=1.9cm, right=1.9cm, top=1.5cm, bottom=1.9cm]{geometry}
---

# Question 1: Applied Engineering degrees (5p)

You want to do a comparative study of the number of awarded applied engineering (civilingenjör) degrees at Chalmers tekniska högskola (Chalmers University of Technology, CTH) and Kungliga tekniska högskolan (The Royal Institute of Technology, KTH) as a function of the academic years. This data is publicly available from the governmental agency Statistiska Centralbyrån (Statistics Sweden). You have been given data on of awarded degrees during the Academic years 1977/78 to 2018/19 in the file `scb_degrees_per_year.csv`, however, in the file the degrees are further split over gender and age.

Part A (2p)
-------------

**Task:** Write a function `read_degree_data(filename)` that can parse files like `scb_degrees_per_year.csv` and return 

1. the labels for the years in a list, and 
2. the result over all years for each combination of school, degree, gender, and age in a dictionary. 


Part B (1p)
-----------

**Task:** Write a function `accumulated_degrees_per_school` that sums the awarded degrees for each school over gender and age and returns a dictionary having the schools as keys and the awarded degrees for all years as values.


Part C (2p)
-----------

**Task:** Write a function `print_degree_table(years, degrees_per_school)` that takes 

* the list `years` with the academic years returned from `read_degree_data` and 
* the dictionary `degrees_per_school` returned from the `accumulated_degrees_per_school` function 

and prints the information in a table with the format:
```
Year    |   CTH    KTH
------------------------
1977/78 |   424    547
1978/79 |   451    593
...
```

Combine the functions into a working script that reads the file, accumulates the grades, and prints the table.
