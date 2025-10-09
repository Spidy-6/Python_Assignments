text1 = input("Enter text to write to the file: ")
with open("Output.txt", "w") as file1:
    file1.write(text1)
    print("Data successfully written to 'Otput.txt'\n")
text2 = "\n" + input("Enter additional text to append: ")
with open("Output.txt", "a") as file2:
    file2.write(text2)
    print("Data successfully appended in 'Output.txt'\n")
with open("Output.txt", "r") as file3:
    file_read = file3.read()
    print(f"Final content of 'Output.txt':\n{file_read}")