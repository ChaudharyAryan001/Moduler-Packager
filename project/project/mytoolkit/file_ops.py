def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print("Data written successfully!")

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found!"