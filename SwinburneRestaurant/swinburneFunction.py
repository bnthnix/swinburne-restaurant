def readItemList(textFile):
    List=[] 
    lines = [line.strip('\n') for line in textFile]
    for line in lines:
        venue={}
        for data in line.split("&"):
            key,value = data.split(":")
            venue[key] = value
        List.append(venue)
    return List
    #Empty list for later append venue dict into it
    #First, make all the lines in the text file into a list
    #For every element in the list, create an empty venue dictionary
    #So that each line represent a new venue
    #for every line, split again, and everything inside it, split again
    #so that the key and venue will go into the dict respectively
    #Append the dict into the list
            
def validateCustomerName(custFirstName,custLastName):
    if custFirstName=="": #Empty input, anything else goes in.
        custFullName=""
        custFileName=""
        ans="No"
    else:
        if custLastName=="-" or custLastName=="":
            custFullName=custFirstName
            custFileName=custFirstName
        else:
            custFullName=custFirstName+" "+custLastName
            custFileName=custLastName
        ans="Yes"
    return ans,custFullName,custFileName
    #Validate customer name
    #if customer do not have first name (wrong input), ans is wrong
    #if customer do not have last name, first name will be used to name file
    #if customer have both, last name will be used to name file
    #last name = surname as requested in the outline

def validateNoOfPeople(people):
    if people.isdigit() and int(people)>=1 and int(people)<=1000:
        ans="Yes"
    else:
        ans="No"
    return ans
    #if input people is digit and more than 0 and less than 1001, correct input

def validateContactNumber(number):
    if number.isdigit() and len(number)==10:
        ans="Yes"
    else:
        ans="No"
    return ans
    #if input number is digit and has 10 character, correct input

def validateVenue(venueChoice,venueList,totalTable):
    if venueChoice=="1" and \
       totalTable<=int(venueList[int(venueChoice)-1]['max']):
        ans="Yes"
    elif (venueChoice=="2" or venueChoice=="3" or \
       venueChoice=="4" or venueChoice=="5" or venueChoice=="6") and \
       totalTable<=int(venueList[int(venueChoice)-1]['max']) and \
       totalTable>int(venueList[int(venueChoice)-2]['max']):
        ans="Yes"
    else:
        ans="No"
    return ans
    #This function is to validate the most suitable venue for customer
    #Only one venue
    #based on total table and the venue choice

def readMenuList(textFile):
    List=textFile.read().split(",")
    return List
    #Read menu text file and append into list
    
def calculateTableTotal(noPeople):
    if int(noPeople)<10:
        totalTable=1
    else:
        totalTable=int(noPeople)//10
        remainder=int(noPeople)%10
        if remainder>5:
            totalTable+=1
    return totalTable
    #to calculate total table
    
def calculateVenuePrice(venueChoice,venueList):
    venuePrice=int(venueList[int(venueChoice)-1]['cost'])
    return venuePrice
    #get venue price from list based on venue chosen
    
def calculateMenuPrice(totalTable,menuChoice,menuList):
    menuPrice=totalTable*int(menuList[int(menuChoice)-1])
    return menuPrice
    #get menu price from list based on menu chosen
    

def calculateEntertainment(entmtChoice,venueChoice,entertainmentList):
    if entmtChoice=="0":
        entertainmentPrice=0
    else:
        entertainmentPrice=int(((entertainmentList[int(venueChoice)-3]\
                                 ["cost"]).split(","))[int(entmtChoice)-1])
    return entertainmentPrice
    #get entmt price from list based on entmt chosen
    #if no entertainment chosen, price=0
    

def calculateTotalPrice(*ALLPRICE): #Arbitrary Argument Lists
    TOTAL=sum(ALLPRICE)
    return TOTAL
    #to calculate total price

def booking(custFileName,custFullName,custNum,noPeople,totalTable,strVenue,\
            strMenu,strEntertainment,totalPrice):
    import datetime,locale
    locale.setlocale(locale.LC_ALL, '')
    now = datetime.datetime.now().strftime("%Y%m%d")
    file=open("Reserved\\{0}_{1}.txt".format(custFileName.replace(" ","_"),now),"w")
    file.write("---------------------\n")
    file.write(" Reservation Summary \n")
    file.write("---------------------\n")
    file.write("Customer Name        : "+custFullName+"\n")
    file.write("Customer Contact No. : "+custNum+"\n")
    file.write("No. of People        : "+noPeople+"\n")
    file.write("No. of Table         : "+str(totalTable)+"\n")
    file.write("Venue                : "+strVenue+"\n")
    file.write("Package              : "+locale.currency(int(strMenu))\
               +" Package"+"\n")
    file.write("Add-On Entertainment : "+strEntertainment+"\n\n")
    file.write("Total Price          : "+str(locale.currency(totalPrice)))
    file.close()
    #.replace(" ","_") cause it is not recommended to have space in file name
    #in programming, coders hate it
    #print reservation summary into text file
    #name the text file based on user name and today's date
    #format total price into local currency
