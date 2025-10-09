try:
    file1 = open('Sample.txt', 'r')
except FileNotFoundError:
    print("Error: The file was not found.")
else:
    fileline1 = file1.readline()
    fileline2 = file1.readline()
    print(f"Reading file content...\nLine 1: {fileline1}Line 2: {fileline2}")
    file1.close()