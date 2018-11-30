# < > with ❤️ by Pranav Sharma


#all neccessary import statements
import urllib3
import json
from time import sleep
import sys
import sqlite3

#disabling a warning related to accessing data securely using urllib3 module
urllib3.disable_warnings()

#connecting to the user database which stores the details of the books that the user has already read
conn = sqlite3.connect('database.db')
c = conn.cursor()

#description text shown to the user
introduction = '''ISBN Book details tracker
Can also be used as a resource for getting information about a book
This can be done using the ISBN number, which is unique to each and every book

Future versions will include features such as GUI, storing book details into database, and 
a book recommendation engine'''

#The first function. This prints out information at the starting of program execution
def welcome():
    print("")
    sleep(1.0)
    print("Welcome to the ISBN Book Facility")
    print("")
    sleep(1.0)

    print("Here are a few things that you can do")
    print("")
    sleep(1.0)

    print("1 : View your collection")
    sleep(1.0)
    print("2 : Add a new book to the database")
    sleep(1.0)
    print("3 : Fetch details about a book")
    sleep(1.0)
    print("4 : Delete a book from the database")
    print("")
    sleep(1.0)

    print("What would you like to do?")
    sleep(1.0)
    print("Enter the number associated with your option!")
    print("")
    sleep(1.0)
    option_input = int(input())
    print("")
    sleep(1.0)

    if(option_input==1):
        sleep(0.5)
        print("You are now viewing your collection!")
        print("")
        readBooks()

    elif(option_input==2):
        print("You have selected Add a new book to the database")
        addBooks()

    elif(option_input==3):
        print("You have selected Fetch Details about a book")
        fetchDetails()

    elif(option_input==4):
        print("You have selected Delete a book from the database")
        deleteBooks()
        
    else:
        print("You enetered invalid option")

def readBooks():
    output = c.execute("SELECT * FROM database")
    sleep(1.0)
    for row in output:
        print("ISBN Number:", row[0])
        print("Date Added:", row[1])
        print("")
        sleep(1.0)

def addBooks():
    isbn_input = int(input("Enter the ISBN Number"))
    date_input = input("Enter today's date in YYYY-MM-DD format")

    c.execute("INSERT INTO database (ISBN_Number, Date_Added) VALUES (?,?)", (isbn_input,date_input))
    conn.commit()
    print("Data has been entered successfully")

def fetchDetails():
    isbn_input = str(input("Enter the ISBN Number"))
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn_input
    
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    response_dict = json.loads(response.data.decode('UTF-8'))
    a=[]

    try:
        a = response_dict['items']
    except KeyError:
        print("")
        sleep(1.0)
        print("Couldn't find book in database")
        print("")
        sleep(1.0)
        quit()
    else:
        b = dict()
        b = a[0]

        print("")
        for c in "LOADING...":
            print(c, end = ' ')
            sys.stdout.flush()
            sleep(0.5)
        print("")
        print("")
        sleep(1.0)

        try:
            title = b['volumeInfo']['title']
        except KeyError:
            print("Title not available")
            print("")
            sleep(1.0)
        else:
            print("Title : ",title)
            print("")
            sleep(1.0)

        try:
            description = b['volumeInfo']['description']
        except KeyError:
            print("Description not available")
            print("")
            sleep(1.0)
        else:
            print("Description : ",description)
            print("")
            sleep(1.0)
        
        try:
            rating = b['volumeInfo']['averageRating']
            ratingCount = b['volumeInfo']['ratingsCount']
        except KeyError:
            print("Rating not available")
            print("")
            sleep(1.0)
        else:
            print("Rating : ",rating, "from", ratingCount, "ratings")
            print("")
            sleep(1.0)
        
        try:
            authors = b['volumeInfo']['authors']
        except KeyError:
            print("Authors not available")
            print("")
            sleep(1.0)
        else:
            print("Authors : ",authors)
            print("")
            sleep(1.0)

        try:
            printType = b['volumeInfo']['printType']
        except KeyError:
            print("Print Type not available")
            print("")
            sleep(1.0)
        else:
            print("Print Type : ",printType)
            print("")
            sleep(1.0)

        try:
            pageCount = b['volumeInfo']['pageCount']
        except KeyError:
            print("Page Count not available")
            print("")
            sleep(1.0)
        else:
            print("Page Count : ",pageCount)
            print("")
            sleep(1.0)
        
        try:
            publisher = b['volumeInfo']['publisher']
        except KeyError:
            print("Publisher not available")
            print("")
            sleep(1.0)
        else:
            print("Publisher : ",publisher)
            print("")
            sleep(1.0)

        try:
            publishedDate = b['volumeInfo']['publishedDate']
        except KeyError:
            print("Publisher not available")
            print("")
            sleep(1.0)
        else:
            print("Published Date : ",publishedDate)
            print("")
            sleep(1.0)

        try:
            webReaderLink = b['accessInfo']['webReaderLink']
        except KeyError:
            print("Web Link not available")
            print("")
            sleep(1.0)
        else:
            print("Web Link : ",webReaderLink)
            print("")
            sleep(1.0)

def deleteBooks():
    output = c.execute("SELECT * FROM database")
    for row in output:
        print("ISBN Number:", row[0])
        print("Date Added:", row[1])
    option = str(input("Do you want to delete all the data (y/n)"))
    if(option=='y'):
        c.execute("DELETE FROM database")
        print("All data deleted successfully")
    else:
        print("You selected No")
        quit()
    

welcome()

