import textGUI
import swinburneFunction

#Print Banner
textGUI.printBanner()

#Input and Validation of Customer's Name
while True:
    custFirstName=input("\nPlease input your First name: ")
    print("If last name is not applicable, please enter a dash \"-\".")
    custLastName=input("Please input your Last name: ")
    ans,custFullName,custFileName=swinburneFunction.validateCustomerName(custFirstName,custLastName)
    if ans=="Yes":
        break
    else:
        print("\nError: Please ensure you entered your surname and given name.")

#Input and Validation of Customer's Phone Number
while True:
    custNum=input("Please enter your phone number: ")
    if swinburneFunction.validateContactNumber(custNum)=="Yes":
        break
    else:
        print("\nError: Please ensure you key in only 10 numbers")

#Input and Validation of Customer's numer of guests ####
while True:
    noPeople=input("Please enter number of people: ")
    if swinburneFunction.validateNoOfPeople(noPeople)=="Yes":
        break
    else:
        print("\nError: Number of people available is within 1 and 1000.")

#Store Venue details into list
venueFile=open("List\\Venue_Cost.txt","r")
venueList=swinburneFunction.readItemList(venueFile)
venueFile.close()

#Print Venue
textGUI.printVenue()

#Calculate total Table based on number of guests entered.
#Will be used to validate venue and calculate price.
totalTable=swinburneFunction.calculateTableTotal(noPeople)

#Select venue and validate whether the venue
#can accommodate the number of table calculated from number of guest entered
while True:
    venueChoice=input("\nPlease select your chosen venue: ")
    if swinburneFunction.validateVenue(venueChoice,venueList,totalTable)=="Yes":
        break
    else:
        print("\nError: Please select the venue that best accommodate \
the number of people you entered.")

#Calculate VENUE PRICE based on venue selected
venuePrice=swinburneFunction.calculateVenuePrice(venueChoice,venueList)

#Read entertainment details into list
entertainmentFile=open("List\\Entertainment_Cost.txt","r")
entertainmentList=swinburneFunction.readItemList(entertainmentFile)
entertainmentFile.close()

#Read menu details into list
menuFile=open("List\\Menu_Package.txt","r")
menuList=swinburneFunction.readMenuList(menuFile)

#Print Menu package list
textGUI.printMenuPackage()
while True:
    menuChoice=input("\nPlease select your menu package to view dishes list: ")
    if menuChoice=="1" or menuChoice=="2" or menuChoice=="3" or \
       menuChoice=="4" or menuChoice=="5" or menuChoice=="6":
        textGUI.printPackage(menuChoice,menuList)
        while True:
            selection=input("\nAnswer: ")
            if selection=="1":
                break
            elif selection=="2":
                print("Please choose another package to view: ")
                textGUI.printMenuPackage()
                break
            else:
                print("\nError: Please enter only the available options.")
        if selection=="1":
            break
    else:
        print("\nError: Please select availalbe menu package.")

#Calculate MENU PRICE based on total table and menu selection
menuPrice=swinburneFunction.calculateMenuPrice(totalTable,menuChoice,menuList)    

if 3<=int(venueChoice)<=6:
    #Print Available Entertainments
    n,AvailableEnt=textGUI.printEntertainment(venueChoice,entertainmentList)
        
    #Calculate ENTERTAINMENT PRICE
    while True:
        entmtChoice=input("\nPlease enter your selection: ")
        if entmtChoice.isdigit() and int(entmtChoice)<n and int(entmtChoice)>=0:
            entertainmentPrice=swinburneFunction.calculateEntertainment(entmtChoice,venueChoice,entertainmentList)
            break
        else:
            print("\nError: Please enter only the available options.")
else:
    entmtChoice="0"
    entertainmentPrice=0

#Calculate total price
totalPrice=swinburneFunction.calculateTotalPrice(venuePrice,menuPrice,entertainmentPrice)

#Display chosen Venue, Menu, Entertainment
strVenue=venueList[int(venueChoice)-1]["name"]
strMenu=menuList[int(menuChoice)-1]
if entmtChoice == "0":
    strEntertainment="None"
else:
    strEntertainment=AvailableEnt[int(entmtChoice)-1]

#Print RESERVATION SUMMARY
textGUI.printSummaryTotal(custFullName,custNum,noPeople,totalTable,strVenue,strMenu,strEntertainment,totalPrice)

#Confirm RESERVATION and WRITE IN TEXTFILE
while True:
    confirm=input("\nDo you want to confirm your reservation?\n[Y]es or [N]o : ")
    if confirm.upper()=="Y":
        swinburneFunction.booking(custFileName,custFullName,custNum,noPeople,totalTable,strVenue,strMenu,strEntertainment,totalPrice)
        print("\nYour reservation has been confirmed. Thank You.")
        break
    elif confirm.upper()=="N":
        print("\nYour reservation has been cancelled.")
        break
    else:
        print("\nError: Please enter the correct option given.")

#To prevent the exe automatically close after the print summary
#input with no variable is used
input("---Press any key to terminate the program---")

#Final comment
#There are still thing that can be modified so that the program can become
#extremly flexible, e.g. in main it has only 6 venue and 6 menue
#which mean it is not flexible enough as 1 to 6 cannot be easily change
#without accesing to the program, which normal human are not recommended to do so
#ideally this all has to have the _name thing, will do it after assignment submission
#it is possible to make them all flexible by using textfile but
#it will take another huge amount of time to do so
#will try them also after submission
