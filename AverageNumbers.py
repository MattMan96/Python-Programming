print("This program averages numbers inside a given file.")
file = input("Enter a filename: ")
answer = 0
number = 0

while file != 'quit':
    infile = open(file, 'r')
    total = 0
    number = 0
    for line in infile:
        number += float(line)
        total += 1
    infile.close()
    answer = number/total
    print("The average is",format(answer,'.2f'))
    file = input("Enter a filename: ")
