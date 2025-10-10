mylist = list(range(1, 11))
print(f"Original list: {mylist}")
thislist = mylist[0:5]
print(f"Extracted first five elements: {thislist}")
thislist.reverse()
print(f"Reversed extracted elements: {thislist}")