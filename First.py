#String concatenation (combine string/text)
f_nm="Viky"
l_nm="Rathore"
full_nm=f_nm+" "+l_nm
print(full_nm)
a=10
b=25
c=a/b
print(c)
sal=2000
sal *=2   # ya     sal = sal*2
print(sal)


#string to interger
raw_input="25"
print(type(raw_input))
age=int(raw_input)
print(type(age))




#Multi factor recruitment eligibility engine
comp_grad=False
cgpa=4.5
if comp_grad:
    if cgpa>=7.5:
        print("Eligible for tech inview rounds")
    else:
        print("Rejected CGPA below requi. crit")
else:
    print("Reject not eligible for interview")



marks_list=[75,82,90,64]
marks_list=[75,82,90,64]




#Loops in Python
#1.For Loop
#2.While
for i in marks_list:
    print(i)
for marks in marks_list:
    print("Students Scored:-", marks)




#2 Range() Function (Running a loop a fixed number of times)
"""Basically it is used for creat a loop to automaticall generate a sequence of numbers.
"""
#Key Rule . The stop value is exclusive . The loop stops exactly before reaching the boundary number.

#1.Start
#2.Stop
#3.Step

#Stop
for i in range(5):
    print(i)
#Start
for i in range(1,5):
    print(i)
#Step
for i in range(2,11,2):
    print(i)



# Counting Backward (Negative Step)
#Rocket launch countdown simulation
#Start at 5, Stop before 0 (stops at 1), step down by -1
for countdown in range(5,0,-1):
    print("T-Minus.....",countdown)
print("Blast off!")

stu_score=[10,20,30,40,50,60,70,80,90,100]
print(len(stu_score))



#Example Running  a loop based on the Length of an Array/List
"""In Data Analytics we often use range (len(array_name)) to loop through data using 
index tracking numbers(0,1,2,3,......) This allow us to modify elements or combine datasets"""
#Dataset
#A Simple list of asset prices
asset_prices=[1000,25000,50000]



#len(asset_princes) is 3 so rnage(3) will generate index numbers: 0,1,2 

for index in range(len(asset_prices)):
    print(f"Item position index: {index} | Asset price : {asset_prices[index]}")
    


#example
#A Basic eg of function with parameter
def check_attendance(student_name):
    print("Verifiying student identity....")
    print(student_name +" is present!")
#calling function
check_attendance("narayan")
check_attendance("Shahil")
check_attendance("Ankita")
#eg
def print_student_id(roll_no,branch):
    print(roll_no ,branch)
#positional 
print_student_id(100, "CSE")
#keywords
print_student_id("ece",1000)






def my_details(age):
    print ("my details is :",my_details)

    my_details(15)