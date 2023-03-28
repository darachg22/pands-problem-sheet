
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            text = f.read()
            num_e = text.count('e')
            print("The file", filename, "contains", num_e, "occurrences of the letter 'e'.")
    except IOError:
        print("Could not read file:", filename)
else:
    print("Please provide a filename as an argument")


