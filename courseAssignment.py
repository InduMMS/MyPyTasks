#Exercise 1: Calculate the multiplication and sum of two numbers 
#Given two integer numbers, write a Python program to return their product 
#only if the product is equal to or lower than 1000. Otherwise, return their sum.
def productBelow1000OrSum(n1, n2):
    print("#### Assignment 1: Calculate the multiplication and sum of two numbers ")
    prod = n1 * n2
    if (prod > 1000): prod = n1 + n2
    return prod

#Exercise 2: Print the Sum of a Current Number and a Previous number
def sumOfCurrentPrev(n):
    print("#### Assignment 2: Print the Sum of a Current Number and a Previous number")
    sum = 0
    for x in range(1,n+1):
        sum = x + (x -1)
        print("Current number: ", x, "  Previous number", (x-1),  "  sum ==", sum )

#Exercise 3: Print characters present at an even index number
def charsAtEvenIndex():
    print("#### Assignment 3: Print characters present at an even index number")
    str = input("Enter a String::")
    for i in range(0,len(str),2):
        print(str[i])

#Exercise 4: Remove first n characters from a string
def removeFirstNChars():
    print("#### Assignment 4: Remove first n characters from a string")
    str = input("Enter a String::")
    #num = int(input("Enter number of chars to be deleted::"))
    num = readANum("Enter number of chars to be deleted::")
    
    str2 = str[num:]
    print("String After deletion::", str2 )


#Exercise 5: Check if the first and last numbers of a list are the same
#Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.
def checkFirstnLastAreSame(lst):
    print("#### Assignment 5: Check if the first and last numbers of a list are the same")
    print(type(lst),"---", lst)
    if (lst[0] == lst[len(lst) -1]): 
        print("Same")
        return True
    else:
        print("Different")
        return False

#Exercise 6: Display numbers divisible by 5
#Write a Python code to display numbers from a list divisible by 5
def printDivByNum(lst, num):
    print("#### Assignment 6: Display numbers divisible by 5")
    print("Original List::", lst)
    modList = []
    for x in lst:
        if (x%num == 0): modList.append(x)
    print("Divisible by ", num, " numbers::", modList)
    
#Exercise 7: Find the number of occurrences of a substring in a string
#Write a Python code to find how often the substring “Emma” appears in the given string.
def findNumOfOccurences(substr, str):
    print("#### Assignment 7: Find the number of occurrences of a substring in a string")
    print("find ", substr, " :: in ::", str )
    num = str.count(substr, 0, len(str))
    print(f"Case sensitive as is Occurs {num} times")

    num = str.lower().count(substr.lower(), 0, len(str))
    print(f"Ignoring case it Occurs {num} times")

#Print the  pattern
def printPattern(num=7):
    print("#### Assignment 8: Print the  pattern")
    print(f"Num : {num}")
    for x in range(1,num+1):
        for k in range(0,x):
            print(x, end=' ')
        print()

#Check Palindrome Number
def checkPalindrome(num):
    print("#### Assignment 9: Check Palindrome Number")
    s1 = str(num)[::-1]
    if (s1 == str(num)):print(f"Number {num} is palindrome")        
    else: print(f"Number {num} is NOT a palindrome")

#Given two lists of numbers, write Python code to create a new list containing 
# odd numbers from the first list and even numbers from the second list.
def genOddFrom1stEvenFrom2nd(list1, list2):
    print("#### Assignment 10: odd numbers from the first list and even numbers from the second list.")
    print("List 1::", list1)
    print("List 2::", list2)
    list3 = [x for x in list1 if x%2!=0]
    list3.extend( [x for x in list2 if x%2==0])
    print("Final List ::", list3)

#Generate Fibonacci series up to 15 terms
def generateFibonacci(num):
    print("#### Assignment 11: Generate Fibonacci series up to 15 terms")
    print(f"Fibonacci series of {num} numbers")
    prev = 0
    next = 1
    print("0, 1",  end=", ")
    for x in range(0,num - 2):
        sum = prev + next
        print(sum, end = ", ")
        prev = next
        next = sum

def readANum(str):
    num = 5
    try:
        num = int(input(str))
    except ValueError as err:
        print(f"got an error {err}. Using default 5")

    return num

if __name__ == "__main__":
    print("when using 167 , 2 ::",productBelow1000OrSum(167,2))    
    print("when using 167 , 6::",productBelow1000OrSum(167,6))
    sumOfCurrentPrev(10)    
    num = input("Enter Number")
    sumOfCurrentPrev(int(num))
    charsAtEvenIndex()
    removeFirstNChars()
    
    checkFirstnLastAreSame( [11, 2, 3, 13, 9, 8, 6, 11] )
    checkFirstnLastAreSame( [11, 2, 3, 13, 9, 8, 6, 12] )    
    printDivByNum( [11, 20, 36, 25, 95, 18, 60, 120, 23, 190, 255] , 5)
    findNumOfOccurences("Emma", "Chellemma this is anEmma, Emmakka! poola remma, koEmma, boemma thallo jEjemma")
    printPattern(5)
    printPattern()
    checkPalindrome(12321)    
    checkPalindrome(1947)
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    genOddFrom1stEvenFrom2nd(list1, list2)
    generateFibonacci(15)
