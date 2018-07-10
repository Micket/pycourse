some_files = [File('Important data.dat', True), File('"Quotes" & jokes.txt', False)]
some_code = [File('important_python_code.py', False), File('cheat_sheet.py', False)]
code_dir = Directory('Code', some_code)
root = Directory('Directories can also have "escaped" characters', some_files)
root.add_node(code_dir)
print(root.xml_structure())
print("Total number of nodes in tree is {}".format(len(root)))
