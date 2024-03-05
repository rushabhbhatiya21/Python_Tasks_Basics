def write_binary_data():
    data = bytes([0x41, 0x42, 0x43, 0x44, 0x45])  # binary data (A, B, C, D, E)

    try:
        with open('test_file.data', 'wb') as file:
            file.write(data)
        print("Binary data has been written to 'test_file.data'")
        file.close()
    except Exception as e:
        print(f"Error writing binary data: {e}")


def read_binary_data():
    try:
        with open('test_file.data', 'rb') as file:
            binary_data = file.read()
            print(f"Read binary data: {binary_data}")
            file.close()
    except FileNotFoundError:
        print("Error: File 'test_file.data' not found.")
    except Exception as e:
        print(f"Error reading binary data: {e}")


write_binary_data()
read_binary_data()
