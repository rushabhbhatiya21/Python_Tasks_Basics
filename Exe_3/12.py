try:
    with open('test_file.txt', 'r') as f:
        for line in f:
            print(line.strip())  # strip to remove new line
except FileNotFoundError:
    print('File not found, check name please!')
