class Myclass:
    x = 10
p1 = Myclass()
print(Myclass.x)    


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

p1 =Person("Ram",20 ,"Jaipur")
print(p1.name)
print(p1.age)
print(p1.address)




#for file read , werite , open 

f= open("student_mat.txt ","r")
print(f.readline())
f.close()
