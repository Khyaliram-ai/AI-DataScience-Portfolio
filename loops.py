# =======  if loop in python   =========
#syntex:
   # if condition:
    #     statement(s)
  # else:
    #     statement(s)


#simple if else
age = 20

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")



#simple if else using pass statement 
age = 20

if age >= 18:
    pass



 # take a inupt then use the if else loop      
user_input = int(input("Enter a age:"))

if user_input >=18:
    print("you are eligible to vote")  
else:
    print("you are not eligible to vote") 





# case of traffic light 
traffic_light = input("Enter the traffic light color (red, yellow, green): ") 

if traffic_light == "green": 
    print("you can go") 
elif traffic_light == "yellow": 
    print("you should stop") 
elif traffic_light == "red": 
    print("you should wait") 
else: 
    print("invalid traffic light color")
print("=========== Execution successfully completed ===========")



# multiple if else statements 
temperature = 25
is_raining = False
is_weekend = True

if(temperature >25 and is_raining == False ) or is_weekend == True:
    print("you can go for a picnic")





#multipal conditon if else statement 
marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")




#Nested if else 
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")




# normal if else 
a=5
b=6
if a<b:print("a is less than b")





# =======  while loop in python   =========
#syntex:
   # starting point
   # while condition:
   #     statement(s)

i=0
while i<6:
    print(i * "o")
    i = i + 1

i1 = 6
while i1>0:
    print(i1 * "@")
    i1 = i1 - 1







# -------------- for loop in python ------------
#syntex:
    # for variable in sequence:
    #     statement(s)  


     
for i in range(1, 6):
    print(i * "*")     

#---- or -----

for i in range(5):
    print(i)




#for loop using list
 
students =["Rahul", "Aman", "Priya"]

for student in students:
    print(student)



#for loop using break statement 
for i in range(10):

    if i== 5:
        break

    print(i)



# for loop using continue statement 
for i in range(5):

    if i == 2:
        continue

    print(i)














