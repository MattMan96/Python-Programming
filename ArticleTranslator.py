print("This program translates articles into more legible English.")
print('Enter the "best" word and its list of synonyms. Type "quit" to end input.')
x = ""
dict1 = {}
list1 = []
total = 0

x = input('')
while x != 'quit':
    x = x.split(' ')
    for index in range(1,len(x)):
        dict1[x[index]] = x[0]
    x = input('')


x = ''

print("")
print('Enter the article one line at a time. Type "quit" to end input.')

x = input('')
while x != 'quit':
    x = x.split(' ')
    list1.append(x)
    x = input('')




for index1 in range(len(list1)):
    for index2 in range(len(list1[index1])):
        word = list1[index1][index2]
        if list1[index1][index2] in dict1.keys():
            del list1[index1][index2]
            list1[index1].insert(index2,dict1[word])

print("")
print("The modified article is as follows:")
for index in range(len(list1)):
    for index2 in range(len(list1[index])):
        if index2 == (len(list1[index])-1):
            print(list1[index][index2])
        else:
            print(list1[index][index2],end = " ")
