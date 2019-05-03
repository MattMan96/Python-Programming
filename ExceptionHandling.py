print("This program averages numbers inside a given file.")
file = input("Enter a filename: ")
answer = 0
number = 0
restart = 0

while file != 'quit':
    try:
        infile = open(file, 'r')
        total = 0
        number = 0
        for line in infile:
            number += int(line)
            total += 1
        answer = number/total
        print("The average is",format(answer,'.2f'))
        file = input("Enter a filename: ")
        infile.close()
            
    except IOError:
        restart = input("Error reading from the file. Try again? (y/n): ")
        if restart == 'y':
            file = input("Enter a filename: ")
        elif restart == 'n':
            quit()
    except ValueError:
        restart = input("The file does not have proper numbers. Try again? (y/n): ")
        if restart == 'y':
            file = input("Enter a filename: ")
        elif restart == 'n':
            quit()
