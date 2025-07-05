#snehith@blockfortrust.com
#https://forms.gle/8LMGcBnA2aFXA354A

import requests
import csv, json

URL = 'https://data.telangana.gov.in/api/1/datastore/query/d72e9ccc-de6a-47e6-96d3-fbc4cd233e73/6'
response = requests.get(URL)
# Check the status code (200 indicates success)
#print(response.content.status_code)

s1 = response.content.decode('utf-8')
print(s1[0:20])
print("INDU")

filename = "data_06_reformed" + ".csv"
file = open(filename, "w", newline='')
cw = csv.writer(file)


#myjson = json.load(response)
myjson = json.loads(s1)

c = rtaHydCz = rtaHydCzTwoSeater = 0
for line in myjson.get("results"):
    #print(str(line))
    
    if c == 0 :
        header = list(line.keys())
        print(" , ".join(header))        
    values = list(line.values())
    #print(" , ".join(values),  values[11], values[6])

    if values[11] == "RTA-HYDERABAD-CZ": 
        print(values[6], "  ", values[11])
        rtaHydCz += 1
        if values[6] == str(2): 
            rtaHydCzTwoSeater += 1

    c += 1
    if c > 50000: break

print("total Lines: ", c)
print("Hyd CZ Registrations:", rtaHydCz, "Two Wheelers: ", rtaHydCzTwoSeater )
file.close()
print ("File opened written & closed successfully!!" , filename)



