# 3. Read a file 'python.txt' which is containing python code and execute the python
# code which is read from the file

with open('python.txt', 'w') as f:
    f.write('print(\'Hello world\')')
    f.close()

with open('python.txt', 'r') as f:
    python_code = f.read()
    exec(python_code)
