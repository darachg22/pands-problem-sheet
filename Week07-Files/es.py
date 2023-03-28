import sys

#Set up command line argument. Used this to learn and practice: https://machinelearningmastery.com/command-line-arguments-for-your-python-script/ 
filename = sys.argv[1]

#The section that reads the file. Research needed to find solution to 'UnicodeDecodeError'. Solution found here: https://sites.pitt.edu/~naraehan/python3/reading_writing_methods.html
#Research and practice led me to the 'as': https://www.w3schools.com/python/ref_keyword_as.asp#:~:text=The%20as%20keyword%20is%20used,using%20c%20instead%20of%20calendar%20. 

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    count = content.count("e")

# The end result
print(f"{count}")