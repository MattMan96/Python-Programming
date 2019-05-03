def uppercase(text):
    count = int(0)

    for char in text:
        if char.isupper():
            count+=1
        
    return(count)

def lowercase(text):
    count = int(0)

    for char in text:
        if char.islower():
            count+=1
    
    return(count)

def digit(text):
    count = int(0)

    for char in text:
        if char.isdigit():
            count+=1
    
    return(count)

def whitespace(text):
    count = int(0)

    for char in text:
        if char.isspace():
            count+=1
    
    return(count)
    
def main():
    end = "quit"
    upper = int(0)
    lower = int(0)
    digits = int(0)
    white = int(0)
    list1 = []
    print('This program analyzes text. Enter text or enter "quit" to quit.')
    text = input("Please enter some text: ")
    while(text != end):
        list1.append(text)
        text = input("Please enter some text: ")
    for line in list1:
        upper = upper + uppercase(line)
        lower = lower + lowercase(line)
        digits = digits + digit(line)
        white = white + whitespace(line)
    print("There are",upper,"uppercase letters in this text.")
    print("There are",lower,"lowercase letters in this text.")
    print("There are",digits,"digits in this text.")
    print("There are",white,"whitespace characters in this text.")

main()
