import sys

#Set up command line argument. Used this to learn and practice: https://machinelearningmastery.com/command-line-arguments-for-your-python-script/ 
filename = sys.argv[1]

#The section that reads the file. Research needed to find solution to 'UnicodeDecodeError'. Solution found here: https://sites.pitt.edu/~naraehan/python3/reading_writing_methods.html
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    count = content.count("e")

# The end result
print(f"{count}")