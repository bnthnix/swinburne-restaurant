from datetime import datetime

def printBanner():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("|                                                                       |")
    print("|                               Welcome to                              |")
    print("|                    Swinburne Restaurant and Lounge                    |")
    print("|                                                                       |")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("Welcome to Swinburne Restaurant and Lounge Reservation Management System")

    import datetime
    #Import datetime to get the date when using this program
    now=datetime.datetime.now()
    print("Today's Date:",now.strftime("%Y-%m-%d"))

def printVenue():
    #Print Venue List from TextFile
    file=open("Display\\Venue_list.txt","r")  #####Max Table
    print(file.read())
    file.close()

def printMenuPackage():
    #Print Menu List from TextFile
    file=open("Display\\Menu_list.txt","r")
    print(file.read())
    file.close()

def printPackage(menuChoice,menuList):
    #Print menu package from TextFile based on user choice
    menu=open("Display\\Menu_{0}.txt".format(menuList[int(menuChoice)-1]),"r")
    print(menu.read())
    menu.close()

def printEntertainment(venueChoice,entertainmentList):
    #Print available entertainment from textFile based on venue choice
    #Using for loop so that number of avaiable entertainment
    #is flexible, textfile can be edited by append more or remove
    #entertainment to certain venue
    AvailableEnt=(entertainmentList[int(venueChoice)-3]["entertainments"]).split(",")
    print("\n--------------------------------------")
    print(" Add-OnEntertainment - ",entertainmentList[int(venueChoice)-3]["venue"])
    print("--------------------------------------\n")
    n=1
    for ent in AvailableEnt:
        print("  "+str(n)+".",ent)
        n+=1
    print("  0. If you do not need add-on entertainment.")
    return n,AvailableEnt

def printSummaryTotal(custFullName,custNum,noPeople,totalTable,\
                      strVenue,strMenu,strEntertainment,totalPrice):
    #Import locale to formate total price to local currency
    #Print the Reservation Summary
    import locale
    locale.setlocale(locale.LC_ALL,'')
    print("\n---------------------")
    print(" Reservation Summary ")
    print("---------------------")
    print("Customer Name        :",custFullName)
    print("Customer Contact No. :",custNum)
    print("No. of People        :",noPeople)
    print("No. of Table         :",totalTable)
    print("Venue                :",strVenue)
    print("Package              :",locale.currency(int(strMenu)),"Package")
    print("Add-On Entertainment :",strEntertainment,"\n")
    print("Total Price          :",locale.currency(totalPrice))
