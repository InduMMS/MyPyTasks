# Online Python 3.12.3 Compiler (Interpreter)
    
import os, random
    
def showCurrentDir():
    contents = os.listdir(os.getcwd())
    for f in contents:
        print(f"file {f},  ")

def generateDataFile():
    datalist = []
    namelist = ["Modi", "Seshu", "Jaya", "Rekha", "Balu", ]
    careerlist = ["Lecturer", "Actor", "Engineer", "Security", "Chef", ]
    for x in range(0,13):
        name = namelist[random.randint(0,x % 5)]
        career = careerlist[random.randint(0,x % 5)]
        datalist.append(str(1000+x) + ',' + name + ',' + career)
    
    #datalist = [['1001', 'Modi', 'PM'], ['1002', 'Amitabh', 'Actor' ] ]
    with open('mydata1.dat', 'w') as datafile:
        for d in datalist:
            print(d)
            #datafile.write(",".join(d))
            datafile.write(str(d) + "\n" )
    datafile.close()

def readDataFile():
    with open(os.getcwd()+ '/' + 'mydata1.dat', 'r') as readfile:
        line = readfile.readline();
        print(line)
        while line:
            line = readfile.read();
            print(line, end="")
    readfile.close()



############################
# Code Execution starts here
############################
print (f"Hi Indu Start Code! {os.getcwd()}" )
showCurrentDir()
generateDataFile()
readDataFile()
print ("End Code!\n")
############################




"""
if os.access(os.getcwd()+ '/' + 'mydata1.dat', os.R_OK):
    print(f"'{os.getcwd()+ '/' + 'mydata1.dat'}' is readable.")
    print(f"'{os.getcwd()+ '/' + 'mydata1.dat'}' size is {os.path.getsize(os.getcwd()+ '/' + 'mydata1.dat')}.")
    os.chmod(os.getcwd()+ '/' + 'mydata1.dat', 0o777)
"""

