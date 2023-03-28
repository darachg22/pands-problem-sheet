# Open the file "HOD.txt" in the same directory as the Python script
with open(r"C:\Users\darac\OneDrive\Desktop\Computing and Data Analytics\pands\pands-problem-sheet\Week07-Files\HOD.txt", "r", encoding="utf-8") as file:
    # Read the contents of the file
    content = file.read()
    print(content)

