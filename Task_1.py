def result (x):
    mydict = {
        "Alice" : 95,
        "Bhupen" : 96,
        "Aman" : 87,
        "John" : 75,
        "Jasmine" : 89
    }
    if x in mydict:
        print(f"{x}'s marks: {mydict[x]}")
    else:
        print(f"Student name {x} not found.")

name = input("Enter a student name: ")
result(name)