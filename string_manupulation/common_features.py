print(r'sumti\thello') # r represents raw string

msg = '''
        Hello,
        My name is sumit kushwah
'''

print(msg)

spam = "sumit kushwah"

print(spam[0:1]) # we can specify a range in string to print no of characters

if "Sumit" in "sumit kushwah":
    print("there is sumit kushwah")

take = input()

if not take.isalpha():
    print("There should not be any blank character")

