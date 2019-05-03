print("This program converts dates.")
date=input("Please enter a date in the form mm/dd/yyyy: ")
mon_list =['No Month','January','February','March','April','May','June','July','August','September','October','November','December']
date_list = list()
index = 0

date_list = date.split('/')

mon_num = date_list[0]
day_num = date_list[1]
year_num = date_list[2]

day_num=int(day_num)
mon_num=int(mon_num)

while index < len(mon_list):
    if mon_num == index:
        mon_num = mon_list[index]
    index+=1




print("The converted date is ",mon_num," ",day_num,", ",year_num,".",sep = '')
