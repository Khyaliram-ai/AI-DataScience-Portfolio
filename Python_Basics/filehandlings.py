#Not automatically closing the file after reading or writing the file and it is done by using open() funcation:
file= open("excalculator.py","r")
print(file)
mycodefile = file.read()
print(mycodefile)
file.close()



#Automatically closing the file after reading or writing the file and it is done by using with open() as file:
with open("sfss.py","r") as file:
    mycodefile = file.read()
    print(mycodefile)



#Automatically closing the file after reading or writing the file and it is done by using with open() as file:
with open("sfss.py","w") as file:
    file.write("print('hello world')")



#readline method 
file =open("sfss.txt","r")
while True:
    line =file.readline()
    print(line)
    if not line:
        print(line,type(line))
        break




with open("sfss.txt","r") as file:
        file.seek(10)
        data =file.read(50)
        print(data)