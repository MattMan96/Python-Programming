##1 Pidm
Term_Code=1
##3 Part of Term Code
##4 Part of Term Desc
##5 Enrolled Ind
##6 Registered Ind
##7 
##8 Student Status Code
##9 Student Status Desc
##10 Level Code
##11 Level Desc
##12 Student Type Code
##13 Student Type Desc
##14 Program Code1
##15 Program Code2
##16 Campus Code
##17 Campus Desc
##18 Department Code
##19 Department Desc
##20 Degree Code1
##21 Degree Desc1
##22 College Code1
##23 College Desc1
##24 Major Code1
##25 Major Desc1
##26 Major Code1 2
##27 Major Desc1 2
##28 Degree Code2
##29 Degree Desc2
##30 College Code2
##31 College Desc2
##32 Major Code2
##33 Major Desc2
##34 Class Code
##35 Class Desc
CRN=35
##37 Reg STS Code
##38 Reg STS Desc
##39 Spec Approval Ind
##40 Reg Error Flag
Subject_Code=40
##42 Subject Desc
##43 Course Number
##44 Section Number
Course_Title=44
##46 Course Level Code
##47 Course Campus Code
##48 Billing Hours
##49 Credit Hours
Instructor_ID=49
Instructor_Name=50
##52 Hours Attended
##53 Grade Mode Code
##54 Grade Mode Desc
##55 Midterm Grade Code
##56 Grade Code
##57 Banner ID
##58 First Name
##59 Last Name
##60 Middle Name
##61 Prefix
##62 Suffix
##63 Preferred First Name
##64 Confid Ind
##65 ACU Email Address
##66 Home Email Address
Begin_Time1=66
End_Time1=67
Bldg_Code1=68
##70 Bldg Desc1
Room_Code1=70
##72 Schd Code1
Monday_Ind1=72
Tuesday_Ind1=73
Wednesday_Ind1=74
Thursday_Ind1=75
Friday_Ind1=76
Saturday_Ind1=77
Sunday_Ind1=78
##80 Begin Time2
##81 End Time2
##82 Bldg Code2
##83 Bldg Desc2
##84 Room Code2
##85 Schd Code2
##86 Monday Ind2
##87 Tuesday Ind2
##88 Wednesday Ind2
##89 Thursday Ind2
##90 Friday Ind2
##91 Saturday Ind2
##92 Sunday Ind2
##93 Advisor1 Term Code Eff
##94 Advisor1 Last Name
##95 Advisor1 First Name
##96 Advisor1 Advisor Code
##97 Advisor1 Primary Advisor Ind
##98 Sport1 Activity Code
##99 Sport1 Code
##100 Sport1 Eligibilty Code
##101 Sport1 Athletic Aid Ind
##102 Sport2 Activity  Code
##103 Sport2 Code
##104 Sport2 Eligibility Code
##105 Sport2 Athletic Aid Ind
##106 Vet Term
##107 Vet Code
##108 Vet Desc
##109 Vet Certified Hours
##110 Vet Certified Date
##111 Vet Certified Hours
##112 Minor Code1
##113 Minor Desc1
##114 Conc Code1
##115 Conc Desc1
##116 Minor Code1 2
##117 Minor Desc1 2
##118 Conc Code1 2
##119 Conc Desc1 2
##120 Minor Code2
##121 Minor Desc2
##122 Rate Code
##123 Ovrall Cumm GPA Hrs Attempted
##124 Ovrall Cumm GPA  Hours Earned
##125 Ovrall Cumm GPA Hrs
##126 Ovrall Cumm GPA Quality Points
##127 Ovrall Cumm GPA
##128 Ovrall Cumm GPA Hrs Passed
##129 Dead Ind
##130 Date Class Added
##131 Registration Status Date
##132 Activity Date
##133 Course College Code
##134 Course College Desc
##135 Course Dept Code
##136 Course Dept Desc
##137 International Ind
##138 Part of Term Start Date
##139 Part of Term End Date
##140 Section Max Enrollment
##141 Section Enrollment
##142 Section Available Seats
##143 Section Schedule Type
##144 Section Instruction Method
##145 Section Session Code
##146 Ipeds Ethnic Code
##147 Ipeds Ethnic Desc




#Given a professor, what is their teaching schedule?
import csv

infile="registration_anon.csv"
classes=[]
try:
 f=open(infile,"r")
 s=f.read()
 count=0
 for list1 in csv.reader(s.splitlines(), skipinitialspace=True):
    classes.append(list1)
 

except:
    print("Error encountered")
    

professors={}

for j in range(1,len(classes)):
    c=classes[j]# current line
    I_ID=c[Instructor_ID] # professor ID number
    if I_ID in professors: # if the professor ID already exists in the dictionary
        crn_found=False
        for i in range(1,len(professors[I_ID])): #         
            if c[CRN] == professors[I_ID][i][0]:
                professors[I_ID][i][1]+=1
                crn_found=True
        if not crn_found:
            professors[I_ID].append([c[CRN],1,c[Term_Code],c[Subject_Code],c[Course_Title],c[Begin_Time1]+"-"+c[End_Time1],c[Bldg_Code1],c[Room_Code1]])
                
    else:
        professors[I_ID]=[c[Instructor_Name],[c[CRN],1,c[Term_Code],c[Subject_Code],c[Course_Title],c[Begin_Time1]+"-"+c[End_Time1],c[Bldg_Code1],c[Room_Code1]]]

for k,v in professors.items(): 
    print("New Professor record:",k) # print out a New Professor record with their ID number
    print("")
    for x in range(len(v)): # find the range for len of v then go through it
        if v[x][7] == '': # this space is for classroom or building. Every once in a while it will be blank
            del v[x][6] # if it is blank then I believe it is an online class so we need to change it.
            v[x].append("Online Class")
            del v[x][6]
        #elif v[x][5] == '-': # this is where begin time and end time usually are but it seems to not want to show for online classes?
           #del v[x][5]  # online classes times would show as "-" so the main goal was to delete it. Unfortuanty at this time it does not work
        print(v[x])
        print("")
    
