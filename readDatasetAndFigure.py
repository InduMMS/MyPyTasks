##readFile = open("TransportVehicleData_01_2019.csv", "r")
c = rtaHydCz = rtaHydCzTwoSeater = 0


with open("TransportVehicleData_01_2019.csv", 'r') as rf:
    for line in rf:
        ##print(line)
        c += 1
        #if c > 50: break
        if c == 0 : print(header)        
        values = line.split(",")

        if values[11] == "RTA-HYDERABAD-CZ": 
            print(values[6], "  ", values[11])
            rtaHydCz += 1
            if values[6] == str(2): 
                rtaHydCzTwoSeater += 1

rf.close()
print ("File opened read & closed successfully!!")

print("total Lines: ", c)
print("Hyd CZ Registrations:", rtaHydCz, "Two Wheelers: ", rtaHydCzTwoSeater )
