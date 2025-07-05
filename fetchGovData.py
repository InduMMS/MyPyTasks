import requests

URL = 'https://data.telangana.gov.in/api/1/datastore/query/d72e9ccc-de6a-47e6-96d3-fbc4cd233e73/'
for i in range(8,15):
    URL = URL + str(i)
    ##URL = "http://www.google.com"
    response = requests.get(URL)
    # Check the status code (200 indicates success)
    print(response.status_code)
    filename = "data_0" + str(i) + ".txt"
    file = open(filename, "w")
    file.write(str(response.content))
    file.close()
    print ("File opened written & closed successfully!!" , filename)



