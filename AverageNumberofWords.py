print('Please enter some sentences. Type "quit" on a line by itself to quit.')
total = int(0)
average = int(0)
list1 = []
word_list=[]
num_word=0

x=input('')

while x != "quit":
    list1.append(x)
    x=input('')
    
for sentance in list1:
    word_list=sentance.split()
    num_word+=len(word_list)
    total+=1
    
average = num_word/total
print("These sentences have an average of",format(average,'.2f'),"words.")
