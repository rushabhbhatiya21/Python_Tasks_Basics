import pickle

integer_var = 42
float_var = 3.14
string_var = "Hello, pickle!"
list_var = [1, 2, 3, 4, 5]
dictionary_var = {'key': 'value', 'name': 'John'}
boolean_var = True


def write_variables(filename):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(integer_var, f)
            pickle.dump(float_var, f)
            pickle.dump(string_var, f)
            pickle.dump(list_var, f)
            pickle.dump(dictionary_var, f)
            pickle.dump(boolean_var, f)
            print("Variables have been dumped to 'my_variables.data'")
            f.close()
    except FileNotFoundError:
        print("No such file or directory")


write_variables('my_variables.data')
