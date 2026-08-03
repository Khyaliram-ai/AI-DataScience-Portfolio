print("Hello")
age =[18,19,20]
nm =["jon","rohan","sonu"]
"jon"
if age[0] ==18 or  nm[0] =="jon":
    if nm[0] =="rj":
        print(" Not choose for driving")

    elif age[0] !=18 or  nm[0] !="jon":
        print("this is avalible in list ")

    else:
        print("this is not valid ")
else:
   print("choose for driving")



   name ="Lavika"
   age1 =20.9646
   age2 =20.9664
   print(f"my name is {name} and my age1 is {age1:.2f} ")
   print(f"my name is {name} and my age1 is {age2:.2f} ")
   print(f"my name is {name} and my age1 is {age2:.3f} ")


   #lists and its operation
   mylist2 =["jon",2,"rohan",4,"shayam","ram",5]
   mylist1 =["apple", "banana", "cherry"]
   mylist1.append("sita")

   print(mylist1[3])

   mylist1.extend(mylist2)
   print(mylist1)





list_a = ["apple", "banana"]
list_b = ["watermalon", "mango"]
extra = ["cherry", "date"]

list_a.append(extra)
print("this is your new list",list_a)

list_a.extend(list_b)
print(list_a)

list_a.remove("date")
print(list_a)

print(list_b)
print(list_a)

print(mylist1)
mylist1.pop(2)
print(mylist1)



list_a.__add__(list_b)
print(list_a)
print(list_b)


#shorting of list
list_b.sort()
print(list_b)