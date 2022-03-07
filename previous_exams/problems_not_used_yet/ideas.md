# question 3/4 OneHotVector
A vector with only 1 nonzero element.


# question 3 eachcolumn 
iterator over a numpy array, give each column at the time. implement repr, len


# question 3 FixedDecimal
self.integral = 123
self.fractional = 456
-> representing 123.456
implement __float__, @staticmethod from_string, __str__, __repr__

implement __lt__ and __eq__  (interesting to consider the fractional part), e.g.
123.456 > 123.3456
123.4560 == 123.456


# This might be to difficult..
implement helper function: @staticmethod split_digits(num, position)
split_digits(1234567, 3) returns (1234, 567)

implement mul, add
123.456 + 456.7891 = 123 + 0.456 + 456 + 0.7891 = 
123 + 456   +   456e-3 + 7891e-4  = 
123 + 456   +   4560e-4 + 7891e-4  =
123 + 456   +   (4560 + 7891) * 1e-4  =
123 + 456   +   (4560 + 7891) * 1e-4  # split apart second part using split_digits

123.456 * 456.7891 = (123 + 0.456) * (456 + 0.789) = 
123 * 456   +   456 * 456 * 1e-3   +   123 * 7891 * 1e-4   +   123 * 7891 * 1e-7
123 * 456   +   456 * 456 * 1e4 * 1e-7   +   123 * 7891 * 1e3 * 1e-4   +   123 * 7891 * 1e0 * 1e-7
123 * 456   +   (456 * 456 * 1e4  +   123 * 7891 * 1e3  +  123 * 7891 * 1e0) * 1e-7


# question 1 "du" like table from directory of files, showing filesize on files and recursively on directories in a nice format
store file hierarchy in dictionary, along with recursive file size

directory: 1.1MiB
├── foo: 200kiB
│   └── file.txt 200kiB
└── bar: 900kiB
   ├── baz.init: 400kiB
   └── foobar.exe: 500kiB 

write function for bytes -> kiB/MiB/GiB 

(indented rendering like that might be a bit difficult)


# question 4: "Series"  (TaylorSeries, FourierSeries)
__iter__ # One term at the time?
__len__ / count
__call__ # implemented using __iter__ in base class
(Quite similar to earlier exam question "CosineSeries")


# question 4: Selection (Circle, Ellipse, Rectangle, Polygon)
__in__ for a given coordinate (tuple)
transform
scale - perhaps different x and y scale? Circle -> Ellipse?
area
(no meaningful shared state or methods though?)


# 
