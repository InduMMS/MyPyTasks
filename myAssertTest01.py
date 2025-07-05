# Online Python 3.12.3 Compiler (Interpreter)
import os
#import requests

class DirNameException(Exception):
    def __init__(self, dir, message='Dir name should be given'):
        self.dir = dir
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}. Provided directory: {self.dir}"
        

def printDir(directory_path):
    try:
        assert len(directory_path) > 0, "Path should be given"
        if len(directory_path) < 4:
            raise DirNameException(directory_path)
    except AssertionError as error:
        print('Handled Assertion Error for path {}', directory_path+'X')
        directory_path = '.'
    except DirNameException as e1:
        print(f"Handled Exception  for path {e1.dir} ::: {e1.message}")
        print(e1)
        directory_path = '.'
        
    try:
       contents = os.listdir(directory_path)
       print(f"Contents of '{directory_path}':")
       #os.system("pip install requests")
       
       for item in contents:
          print(item)
    except OSError as e:
       print(f"Error: Failed to list contents of directory '{directory_path}'. {e}")

def getData(api):
    r = requests.get(url = URL)
    print(r.json())
    

def main():
    print ("Hello, INDU!\n")
    dp = printDir('')
    dp = printDir('zz')
    dp = os.getcwd()
    printDir(dp)
    api = "https://data.telangana.gov.in/api/1/metastore/schemas/dataset/items/d72e9ccc-de6a-47e6-96d3-fbc4cd233e73/docs"
    #getData(api)
    print ("\nBye, INDU!\n")
    
if __name__ == '__main__':
    main()
