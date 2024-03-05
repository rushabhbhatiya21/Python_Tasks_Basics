import pickle


def load_variables(filename):
    try:
        with open(filename, 'rb') as f:
            loaded_integer_var = pickle.load(f)
            loaded_float_var = pickle.load(f)
            loaded_string_var = pickle.load(f)
            loaded_list_var = pickle.load(f)
            loaded_dictionary_var = pickle.load(f)
            loaded_boolean_var = pickle.load(f)
            return loaded_integer_var, loaded_float_var, loaded_string_var, loaded_list_var, loaded_dictionary_var, loaded_boolean_var
    except FileNotFoundError:
        print("No such file or directory")


loaded_integer_var, loaded_float_var, loaded_string_var, loaded_list_var, loaded_dictionary_var, loaded_boolean_var = load_variables(
    'my_variables.data')

print(f"Loaded Integer Variable: {loaded_integer_var}")
print(f"Loaded Float Variable: {loaded_float_var}")
print(f"Loaded String Variable: {loaded_string_var}")
print(f"Loaded List Variable: {loaded_list_var}")
print(f"Loaded Dictionary Variable: {loaded_dictionary_var['name']}")
print(f"Loaded Boolean Variable: {loaded_boolean_var}")
