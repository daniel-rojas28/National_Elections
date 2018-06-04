# Register / Login
users =[]
partities =[]
province=[]
ballotP = []
provincesAvailable = province

def main():
    print("Hello")
    choice=(input("(1)Register    (2)Login\n"))
    if choice == "1":
        RegisterUI()
    elif choice == "2":
        loginUI()
    else:
        print("Unexpected value, please try again")
        main()


def Register(name, id, email, age, password, passwordConfirm, admin):
    x = 0
    if password == passwordConfirm:
       i = 0
       while i < len(users):
            if users[i]['Id'] != id and users[i]['Email'] != email:
                x += 1
            i += 1
       if x == len(users):
           if admin == "Yes":
               newuser = {"Name": name, "Email": email, "Password": password, "Age": age, "Id": id, "Admin": True}
               users.append(newuser)
               return True
           else:
               newuser = {"Name": name, "Email": email, "Password": password, "Age": age, "Id": id, "Admin": False}
               users.append(newuser)
               return True
       else:
           return ("user exist")
    else:
        return ("password")


def RegisterUI():
    name = str(input("Enter your name: "))

    validId = False
    while validId == False:
        try:
            id = int(input("Enter your id: "))
            break;
        except ValueError:
            print("You must enter numbers")
    email = str(input("Enter your email: "))

    validAge = False
    while validAge == False:
        try:
            age = int(input("Enter your age: "))
            break;
        except ValueError:
            print("You must enter numbers")

    password = str(input("Enter your password: "))

    passwordConfirm = str(input("Confirm the password: "))

    response = isAdmin();
    if response == True:
        admin = "Yes"
    elif response == False:
        admin = "No"

    if ((name == "") or (id == "") or (email == "") or (age == "") or (password == "") or
            (passwordConfirm == "") or (admin == "")):
        print("Empy slots are not permited");
        RegisterUI()
    else:
        request = Register(name, id, email, age, password, passwordConfirm, admin)

    if (request == True):
        print("\n"*10)
        print("User Register! Congratulation")
        main()
    elif (request == "password"):
        print("Passwords are not equals, try again")
        RegisterUI()
    elif (request == "user exist"):
        print("The user already exist, please try again")
        RegisterUI()

def isAdmin():
    print("Are you Admin?")
    choice = (input("(1)Yes   (2)No\n"))
    if choice == "1":
        return True
    elif choice == "2":
        return False
    else:
        print("Unexpected value, please try again")
        isAdmin()

def login(id, password):
    if len(users) == 0:
        return "no users"
    i = 0
    while i < len(users):
        if users[i]["Id"] == id and users[i]["Password"] == password:
            userAdmin = users[i]["Admin"]
            userName = users[i]["Name"]
            return ("True", userAdmin, userName)
        elif users[i]["Id"] == id and users[i]["Password"] != password:
            return ("password error")
        i += 1
    return "no users"

def loginUI():
    validId = False
    while validId == False:
        try:
            id = int(input("Enter your id: "))
            break;
        except ValueError:
            print("You must enter numbers")

    password = str(input("Enter your password: "))

    response = login(id, password)
    admin = response[1]
    name = response[2]
    if response[0] == "True":
        if admin == True:
            print("\n" * 10)
            print("Welcome"+" "+str(name)+"!")
            adminMenu()
        elif admin == False:
            print("\n" * 10)
            print("Welcome" + " " + str(name) + "!")
            guestMenu()
    elif response == "password error":
        print("\n" * 10)
        print("Invalid Password")
        loginUI()
    else:
        print("\n" * 10)
        print("The User no exist")
        main()

def adminMenu():
    choice = (input("(1)Territorial Distribution (2)Partities Administration (3)Ballots Administration "
                    "(4)Results (5)Queries (6)Back\n"))
    if choice == "2":
        print("\n"*10)
        partitiesAdministration()
    elif choice == "1":
        print("\n"*10)
        territorialDistribution()
    elif choice == "3":
        print("\n" * 10)
        mainBallots()
    elif choice == "4":
        print("\n"*10)
        resultsMenu()
    elif choice == "5":
        queries()

def guestMenu():
    choice = (input("(1)Queries (6)Back\n"))


def partiesAdministration():
    choice = (input("(1)Create Partie (2)Edit Partie (3)Delete Partie (4)Back\n"))
    if choice == "1":
        createPartitieUI()
    elif choice == "2":
        if partities == []:
            print("\n"*10)
            print("No have parties")
            partitiesAdministration()
        else:
            print("\n" * 10)
            editPartitie()
    elif choice == "3":
        if partities == []:
            print("\n" * 10)
            print("No have parties")
            partitiesAdministration()
        else:
            print("\n" * 10)
            deletePartitie()
    elif choice == "4":
        adminMenu()
    else:
        print("Unexpected value, please try again")
        partitiesAdministration()

def createPartitie(name, since, colors, idology):
    x = 0
    i = 0
    while i < len(partities):
        if partities[i]['Name'] != name:
            x += 1
        i += 1
    if x == len(partities):
            newpartitie = {"Name": name, "Since": since, "Colors": colors, "Idology": idology, "Votes": []}
            partities.append(newpartitie)
            return True
    else:
        return ("partitie exist")

def createPartitieUI():
    name = str(input("Enter partie name: ")).upper()

    validAge = False
    while validAge == False:
        try:
            age = int(input("Enter age of fundation: "))
            break;
        except ValueError:
            print("You must enter numbers")

    colors = str(input("What are the colors for this partities? "))

    idology = str(input("What idology this partie have? "))

    if ((name == "") or (age == "") or (colors == "") or (idology == "")):
        print("\n"*10)
        print("Empy slots are not permited")
        createPartitieUI()
    else:
        request = createPartitie(name, age, colors, idology)

    if request == True:
        print("\n" * 10)
        print("The partie are created")
        partitiesAdministration()
    elif request == "partitie exist":
        print("\n" * 10)
        print("The partie already exist")
        partitiesAdministration()

def editPartitie():
    partitiesStr = ""
    i = 0
    while i < len(partities):
        partitiesStr = partitiesStr + "("+str(i)+")"+partities[i]["Name"]+" "
        i += 1
    print("Select the partie you like edit")
    choice = int((input(partitiesStr + " "+ "(" + str(len(partities)) + ")" + "Back" + "\n")))
    if choice >= len(partities):
        print("Unexpected value, please try again")
        editPartitie()
    elif choice == len(partities):
        editPartitie()
    else:
        name = str(input("Enter partie name: "))

        validAge = False
        while validAge == False:
            try:
                age = int(input("Enter age of fundation: "))
                break;
            except ValueError:
                print("You must enter numbers")

        colors = str(input("What are the colors for this parties? "))

        idology = str(input("What idology this partitie have? "))

        if ((name == "") or (age == "") or (colors == "") or (idology == "")):
            print("Empy slots are not permited")
            createPartitieUI()
        else:
            partities[choice]["Name"] = name
            partities[choice]["Since"] = age
            partities[choice]["Colors"] = colors
            partities[choice]["Idology"] = idology
            print("Change Saved")
            partitiesAdministration()

def deletePartitie():
    partitiesStr = ""
    i = 0
    while i < len(partities):
        partitiesStr = partitiesStr + "(" + str(i) + ")" + partities[i]["Name"] + " "
        i += 1
    print("Select the partitie you like remove")
    choice = int((input(partitiesStr + " "+ "(" + str(len(partities)) + ")" + "Back" + "\n" )))
    if choice > len(partities):
        print("Unexpected value, please try again")
        deletePartitie()
    elif choice == len(partities):
        partitiesAdministration()
    else:
        partities.pop(choice)
        print("\n"*10)
        print("The partie has eliminated")
        partitiesAdministration()




def ADD():
    print("What do you want to add to list?")
    choice1 = input("Do you want to add... (1)Province    (2)Canton   (3)District   or (4)Back\n")
    if choice1 == "1":  # Add Province
        addProvince()
    elif choice1 == "2":  # Add Canton
        addCanton()
    elif choice1 == "3":  # Add District
        addDistricts()
    elif choice1 == "4":   #Return to main
        territorialDistribution()
    else:
        print("Invalid option")
        ADD()

def MODIFY():
    print("\n"*10)
    def modifyProvince():

        a = 0
        print("List of provinces:")
        while a < len(province):
            print(str(a+1)+ "-) "+ str(province[a]["name"]) +" with " + str(province[a]["deputies"])+" deputies")
            a += 1
        action=input("(1)Rename (2)Change deputies  (3)Exit\n")
        if action == "1":
            invalidValue = False
            while invalidValue == False:
                try:
                    num = int(input("#Province: "))
                    break
                except ValueError:
                    print("You most use numbers")
            if num-1 < len(province):
                newName = input("New name: ").title()
                province[num - 1]["name"] = newName
                print("Successful Change")
                modifyProvince()
            else:
                print("Invalid option")
                modifyProvince()

        elif action == "2":
            invalidValue = False
            while invalidValue == False:
                try:
                    pro = int(input("#Province: "))
                    break
                except ValueError:
                    print("You must use numbers")
            if pro-1 < len(province):
                while invalidValue == False:
                    try:
                        newCant = int(input("# of deputies: "))
                        break
                    except ValueError:
                        print("You must use numbers")

                province[pro - 1]["deputies"] = newCant
                print("Successful Change")
                modifyProvince()
            else:
                print("Invalid option")
                modifyProvince()


        elif action== "3":
            MODIFY()
        else:
            print("Invalid option")
            modifyProvince()

    def modifyCantons():

        a = 0
        print("List of provinces:")
        while a < len(province):
            print(str(a + 1) + "-) " + str(province[a]["name"]))
            a+=1
        respond=input("(1)Change (2)Exit")
        if respond=="1":
            invalidOption = False
            while invalidOption == False:
                try:
                    numP = int(input("From which province you want to change the cantons?\n #Province: "))
                    break
                except ValueError:
                    print("You must use numbers")

            if numP-1<len(province):
                b=0
                if len(province[numP-1]["cantons"])!= 0:
                    print("List of cantons from "+ province[numP-1]["name"])
                    while b < len(province[numP-1]["cantons"]):
                        print(str(b+1)+"-) "+str(province[numP - 1]["cantons"][b]["name"]))
                        b += 1
                    validValue=False
                    while validValue==False:
                        try:
                            nomC = int(input("#Canton"))
                            break
                        except ValueError:
                            print("You must use numbers")

                    if nomC - 1 < len(province[numP - 1]["cantons"]):
                        newC = input("New name: ").title()
                        while newC == "":
                            print("Unexpected value")
                            newC = input("New name: ").title()
                        province[numP - 1]["cantons"][nomC - 1]["name"] = newC
                        print("Successful Change")
                        choice = (input("Keep Modyfing Cantons (Y/N)?\n"))
                        if choice == "y" or choice == "Y":
                            modifyCantons()
                        else:
                            MODIFY()
                    else:
                        print("Invalid option")
                        modifyCantons()

                else:
                    print("No cantons")
                    modifyCantons()
            else:
                print("Option not in list")
                modifyCantons()
        elif respond == "2":
            MODIFY()
        else:
            print("Invalid option")
            modifyCantons()

    def modifyDistricts():

        a = 0
        print("List of provinces:")
        while a < len(province):
            print(str(a + 1) + "-) " + str(province[a]["name"]))
            a += 1
        respond = input("(1)Change (2)Exit")
        if respond == "1":
            invalidOption=False
            while invalidOption == False:
                try:
                    numP=int(input("From which province you want to change the districts?\n#Province: "))
                    break
                except ValueError:
                    print("You must use numbers")

            if numP-1 < len(province):
                b = 0
                if len(province[numP - 1]["cantons"]) != 0:
                    print("List of cantons from " +str(province[numP - 1]["name"]))
                    while b < len(province[numP - 1]["cantons"]):
                        print(str(b + 1) + "-) " + str(province[numP - 1]["cantons"][b]["name"]))
                        b += 1
                    while invalidOption == False:
                        try:
                            numC= int(input("From which canton you want to change the districts?\n#Canton"))
                            break
                        except ValueError:
                            print("You must use numbers")

                    if numC-1<len(province[numP-1]["cantons"]):
                        print("List of districts from " + str(province[numP-1]["name"]) + "(" + str(province[numP-1]["cantons"][numC-1]["name"] + ")"))
                        c=0
                        if len(province[numP-1]["cantons"][numC-1]["districts"])!=0:
                            while c<len(province[numP-1]["cantons"][numC-1]["districts"]):
                                print(str(c+1) + "-)" + str(province[numP-1]["cantons"][numC-1]["districts"][c]))
                                c+=1
                            while invalidOption == False:
                                try:
                                    numD=int(input("#District: "))
                                    break
                                except ValueError:
                                    print("You must use numbers")

                            if numD-1<len(province[numP-1]["cantons"][numC-1]["districts"]):
                                newD=input("New name: ").title()
                                while newD=="":
                                    print("No name")
                                    newD = input("New name: ").title()
                                province[numP - 1]["cantons"][numC - 1]["districts"][numD - 1] = newD
                                print("Successful Change")
                                choice = (input("Keep Modyfing Districts (Y/N)?\n"))
                                if choice == "y" or choice == "Y":
                                    modifyDistricts()
                                else:
                                    MODIFY()
                            else:
                                print("Invalid options")
                                modifyDistricts()
                        else:
                            print("No districts")
                            modifyDistricts()
                    else:
                        print("Invalid option")
                        modifyDistricts()
                else:
                    print("No cantons")
                    modifyDistricts()
            else:
                print("Invalid option")
                modifyDistricts()

        elif respond == "2":
            MODIFY()
        else:
            print("Invalid option")
            modifyDistricts()

    if len(province)!=0:#Menu from MODIFY
        choice=input("What do you want to modify?"+" (1)Provinces   (2)Cantons  (3)District     or (4)Back to menu\n")
        if choice == "1":
            modifyProvince()
        elif choice == "2":
            modifyCantons()
        elif choice == "3":
            modifyDistricts()
        elif choice == "4":
            territorialDistribution()
        else:
            print("Invalid Option")
            MODIFY()
    else:
        print("No values to modify")
        territorialDistribution()


def DELETE():

    def deleteProvince():

        a = 0
        print("List of provinces:")
        while a < len(province):
            print(str(a + 1) + "-) " + str(province[a]["name"]))
            a += 1
        invalidOption=False
        while invalidOption == False:
            try:
                numP = int(input("Which province you want to delete?\n #Province: "))
                break
            except ValueError:
                print("You must use numbers")

        if numP-1 <len(province):
            del province[numP-1]
            print("\n" * 10)
            print("Successfully deleted")
            DELETE()

        else:
            print("Invalid option")
            deleteProvince()

    def deleteCanton():

        print("***If you delete an canton, districts inside will be deleted too***")
        a = 0
        print("List of provinces:")
        while a < len(province):
            print(str(a + 1) + "-) " + str(province[a]["name"]))
            a += 1
        invalidValue = False
        while invalidValue == False:
            try:
                numP = int(input("From which province you want to delete cantons ?\n #Province: "))
                break
            except ValueError:
                print("You must use numbers")
        if numP - 1 < len(province):
            b = 0
            if len(province[numP - 1]["cantons"]) != 0:
                print("List of cantons from " + str(province[numP - 1]["name"]))
                while b < len(province[numP - 1]["cantons"]):
                    print(str(b + 1) + "-) " + str(province[numP - 1]["cantons"][b]["name"]))
                    b += 1
                while invalidValue==False:
                    try:
                        numC= int(input("Which canton you want to delete? \n #Canton: "))
                        break
                    except ValueError:
                        print("You must use numbes")
                if numC - 1 < len(province[numP - 1]["cantons"]):
                    del province[numP - 1]["cantons"][numC - 1]
                    print("\n" * 10)
                    print("Successfully deleted")
                    DELETE()
            else:
                print("No cantons in "+ str(province[numP-1]["name"]))

        else:
            print("Invalid option")
            deleteCanton()

    def deleteDistricts():

        a = 0
        print("List of provinces:")
        while a < len(province):
            print(str(a + 1) + "-) " + str(province[a]["name"]))
            a += 1
        invalidValue = False
        while invalidValue == False:
            try:
                numP = int(input("From which province you want to delete districts ?\n #Province: "))
                break
            except ValueError:
                print("You must use numbers")
        if numP - 1 < len(province):
            b = 0
            if len(province[numP - 1]["cantons"]) != 0:
                print("List of cantons from " + str(province[numP - 1]["name"]))
                while b < len(province[numP - 1]["cantons"]):
                    print(str(b + 1) + "-) " + str(province[numP - 1]["cantons"][b]["name"]))
                    b += 1
                while invalidValue==False:
                    try:
                        numC=int(input("From which canton of "+ "\n#Canton: "))
                        break
                    except ValueError:
                        print("You must use numbers")

                if province[numP - 1]["cantons"][numC - 1] != 0:
                    if numC < len(province[numP - 1]["cantons"][numC - 1]):
                        c = 0
                        while c < len(province[numP - 1]["cantons"][numC - 1]["districts"]):
                            print(str(c + 1) + "-)" + str(
                                province[numP - 1]["cantons"][numC - 1]["districts"][c]))
                            c += 1

                        while invalidValue == False:
                            try:
                                numD = int(input("Which district you want to delete?\n #District"))
                                break
                            except ValueError:
                                print("You must use numbers")
                        if numD-1 < len(province[numP - 1]["cantons"][numC - 1]["districts"]):
                            del province[numP - 1]["cantons"][numC - 1]["districts"][numD - 1]
                            print("\n" * 10)
                            print("Successfully deleted")
                            DELETE()
                        else:
                            print("Invalid option")
                            deleteDistricts()

                else:
                    print("No districts")
                    deleteDistricts()


            else:
                print("No cantons, no districts")
                deleteDistricts()
        else:
            print("Invalid option")
            deleteDistricts()


    if len(province)!=0:
        choice=input("What do you want to delete?\n(1)Province  (2)Canton   (3)Districts (4)Back\n")
        if choice == "1":
            deleteProvince()
        elif choice == "2":
            deleteCanton()
        elif choice == "3":
            deleteDistricts()
        elif choice == "4":
            territorialDistribution()
    else:
        print("No values to delete")
        territorialDistribution()



def addProvince():

    print("\n"*10)
    nameP = input("Province's name: ").title()
    while nameP == "":
        print("No province's name")
        nameP = input("Province's name: ").title()

    invalidValue=False
    while invalidValue==False:
        try:
            cantD = int(input("How many deputies does " + str(nameP) + " have? "))
            break
        except ValueError:
            print("Must be numbers")
    x = 0
    if len(province) != 0:
        while x < len(province):
            if nameP in province[x]["name"]:
                print("/" * 10 + str(nameP) + " it's already in list " + "/" * 10)
                ADD()

            else:
                x += 1
        newP = {"name": nameP, "deputies": cantD, "cantons": [], "ballotP": [], "ballotL": []}
        province.append(newP)
        ans = input("Keep adding? (Y/N)")
        if ans == "y" or ans == "Y":
            ADD()
        else:
            territorialDistribution()
    else:
        newP = {"name": nameP, "deputies": cantD, "cantons": [], "ballotP": [], "ballotL": []}
        province.append(newP)
        ans = input("Keep adding? (Y/N)")
        if ans == "y" or ans == "Y":
            ADD()
        else:
            territorialDistribution()

def addCanton():

    if province == []:
        print("\n" * 10)
        print("No provinces to add canton")
        ADD()
    else:
        nameC = input("Canton's name: ").title()
        while nameC == "":
            print("No canton's name")
            nameC = input("Canton's name: ").title()
        newC = {"name": nameC, "districts": [], "ballotP": [], "ballotL": []}
        a = 0
        provinces = ""
        while a < len(province):
            provinces = provinces + str(province[a]["name"])+ " "
            a += 1
        print(provinces)
        location = input("Where this canton  comes from?").title()
        i = 0
        if len(province) != 0:
            while i < len(province):
                if province[i]["name"] == location:
                    province[i]["cantons"].append(newC)
                    ans = input("Keep adding? (Y/N)")
                    if ans == "y" or ans == "Y":
                        ADD()
                    else:
                        territorialDistribution()
                else:
                    if i + 1 == len(province):
                        print("Unexpected location, try again")
                        addCanton()
                    elif i <= len(province):
                        i += 1
        else:
            print("There is no province where to add canton")
            ADD()


def addDistricts():
    if province == []:
        print("\n"*10)
        print("No provinces to add distrit")
        ADD()
    else:
        nameD = input("District's name: ").title()
        newD={"name":nameD, "ballotsP":[], "ballots":[]}
        while nameD == "":
            print("No district's name")
            nameD = input("District's name: ").title()
        count1 = 0
        while count1 < len(province):
            count2=0
            while count2 < len(province[count1]["cantons"]):
                count3 = 0
                while count3 < len(province[count1]["cantons"][count2]["districts"]):
                    if province[count1]["cantons"][count2]["districts"][count3]["name"] == nameD:
                        print("\n"*10)
                        print(str(nameD) + " its already in list")
                        addDistricts()
                    else:
                        count3 += 1
                count2 += 1
            count1 += 1
        provinces = ""
        a = 0
        while a < len(province):
            provinces = provinces + str(a)+"-) " +  str(province[a]["name"]) + ""
            a += 1
        print(provinces)

        locationP = int(input("To which PROVINCE does it belong?\n #Province"))
        j = 0
        if len(province) != 0:
            while j < len(province):
                if locationP<len(province):
                    cantons = ""
                    a = 0
                    while a < len(province):
                        b = 0
                        while b < len(province[a]["cantons"]):
                            cantons= cantons +  str(province[locationP]["cantons"][b]["name"])
                            b += 1
                        a += 1
                    print (cantons)
                    locationC = input("To which CANTON does it belong?").title()
                    while locationC == "":
                        print("Canton's name required")
                        locationC = input("To which CANTON does it belong?").title()
                    k = 0
                    if len(province[j]["cantons"]) != 0:
                        while k < len(province[j]):
                            if province[j]["cantons"][k]["name"] == locationC:
                                province[j]["cantons"][k]["districts"].append(newD)
                                ans = input("Keep adding? (Y/N)")
                                if ans == "y" or ans == "Y":
                                    ADD()
                                else:
                                    territorialDistribution()
                            else:
                                if k + 1 == len(province[j]["cantons"]):
                                    print("Unexcpected location, try again")
                                    addDistricts()
                                elif k < len(province[j]):
                                    k += 1
                        break
                    else:
                        print("There is no canton where to add district")
                        ADD()

                else:
                    if j + 1 == len(province):
                        print("Unexpected location")
                        addDistricts()
                    elif j <= len(province):
                        j += 1
        else:
            print("There is no province where to add district")
            print("Try again")
            ADD()






def SHOW():
    print("\n" * 10)
    a = 0
    while a < len(province):
        print(str(province[a]["name"]) +" with " + str(province[a]["deputies"])+" deputies")
        b = 0
        while b < len(province[a]["cantons"]):
            print("     -"+province[a]["cantons"][b]["name"])
            c = 0
            while c < len(province[a]["cantons"][b]["districts"]):
                print("         +"+province[a]["cantons"][b]["districts"][c])
                c += 1
            b += 1
        a += 1
    print(province)
    territorialDistribution()

def territorialDistribution():
    print("Welcome to Territorial Distribution Manager")
    print("-------------------------------------------")
    print("What you want to do?")

    choice = input("(1)Add    (2)Modify   (3)Delete    (4)Show Data (5)Back\n")

    if choice == "1":
        ADD()
    elif choice == "2":
        MODIFY()
    elif choice == "3":
        DELETE()
    elif choice == "4":
        SHOW()
    elif choice == "5":
        adminMenu()
    else:
        print("Unexpected value, please try again")
        territorialDistribution()


def mainBallots():
    def createBallotP():
        partitiesBallotP = partities[:]
        if ballotP == []:
            option = True
            while option == True:
                if partitiesBallotP != []:
                    a = 0
                    while a < len(partitiesBallotP):
                        print(str(a) + "-) " + partitiesBallotP[a]["Name"])
                        a += 1
                    invalidOption = False
                    while invalidOption == False:
                        try:
                            addPartitie = int(input("Which partitie you want to add to the PRESIDENTIAL BALLOT\n"))
                            break
                        except ValueError:
                            print("You must use numbers")
                    if addPartitie < len(partitiesBallotP):
                        extract = partitiesBallotP.pop(addPartitie)
                        ballotP.append(extract)
                        i = 0
                        while i < len(province):
                            j = 0
                            while j < len(province[i]["cantons"]):
                                k = 0
                                while k < len(province[i]["cantons"][j]["districts"]):
                                    province[i]["cantons"][j]["districts"][k]["ballots"] = ballotP
                                    k += 1
                                j += 1
                            i += 1
                        choice = input("Keep adding? (Y/N)")
                        if choice == "y" or choice == "Y":
                            option = True
                        else:
                            mainBallots()
                    else:
                        print("\n" * 10)
                        print("Invalid option")
                        addBallots()
                else:
                    print("All partities was added, ballot created")

                    addBallots()
        else:
            print("\n" * 10)
            print("Presidential ballot already created")
            addBallots()

    def modifyBallotP():
        if ballotP != []:
                copyPartities = []
                a=0
                while a < len(ballotP):
                    print(str(a) + "-) " + str(ballotP[a]["Name"]))
                    a+=1
                choice= input("(1)Add partities or (2)Delete partities ")
                if choice == "1":
                    for num in partities:
                        if num not in ballotP:
                            copyPartities.append(num)
                    option = True
                    while option == True:
                        if copyPartities != []:
                            z=0
                            while z< len(copyPartities):
                                print(str(z) + "-) " + str(copyPartities[z]["Name"]))
                                z+=1
                            invalidPartitie = False
                            while invalidPartitie == False:
                                try:
                                    numPartitie = int(input("Which partitie you want to add"))
                                    break
                                except ValueError:
                                    print("You must use numbers")
                            if numPartitie<=len(copyPartities):
                                extract=copyPartities.pop(numPartitie)
                                ballotP.append(extract)
                                choice= input("Keep modifying Presidential\n")
                                if choice == "y" or choice == "Y":
                                    option = True
                                else:
                                    modifyBallots()
                            else:
                                print("Invalid option")
                                modifyBallotP()
                        else:
                            print("No partities to add, changes saved")
                            modifyBallots()



                elif choice == "2":
                    option = True
                    while option == True:
                        try:
                            choice = int(input("Which partitie you want to delete"))
                        except ValueError:
                            print("You must use numbers")
                        if choice< len(ballotP):
                            break
                    ballotP.pop(choice)
                    print("Successfully Deleted")
                    ans= input("Keep deleting?")
                    if ans == "y" or ans == "y":
                        modifyBallotP()

                    else:
                        modifyBallots()

                else:
                    print("Invalid option")
                    modifyBallotP()
        else:
            print("The Presidential ballot have not been created yet")
            modifyBallots()

    def modifyBallotL():
        if province != []:
            a=0
            while a< len(province):
                print(str(a) + "-) "+ str(province[a]["name"]))
                a+=1
            invaidNumber = False
            while invaidNumber == False:
                try:
                    numberP= int(input("From which province you want to modify Legislative Ballot? \n#Province: "))
                except ValueError:
                    print("You mus use numbers")
                if numberP<len(province):
                    break
            if province[numberP]["ballotL"] != []:
                a = 0
                while a < len(province[numberP]["ballotL"]):
                    print(str(a) + "-) " + str(province[numberP]["ballotL"][a]["Name"]))
                    a+=1
                copyPartities=[]
                choice = input("(1)Add partities or (2)Delete partities ")
                if choice == "1":
                    for num in partities:
                        if num not in province[numberP]["ballotL"]:
                            copyPartities.append(num)
                    option = True
                    while option == True:
                        if copyPartities != []:
                            z = 0
                            while z < len(copyPartities):
                                print(str(z) + "-) " + str(copyPartities[z]["Name"]))
                                z += 1
                            invalidPartitie = False
                            while invalidPartitie == False:
                                try:
                                    numPartitie = int(input("Which partitie you want to add"))
                                    break
                                except ValueError:
                                    print("You must use numbers")
                            if numPartitie <= len(copyPartities):
                                extract = copyPartities.pop(numPartitie)
                                province[numberP]["ballotL"].append(extract)
                                choice = input("Keep modifying Presidential\n")
                                if choice == "y" or choice == "Y":
                                    option = True
                                else:
                                    modifyBallots()
                            else:
                                print("Invalid option")
                                modifyBallotP()
                        else:
                            print("No partities to add, changes saved")
                            modifyBallots()
                elif choice == "2":
                    option = True
                    while option == True:
                        try:
                            choice = int(input("Which partitie you want to delete"))
                            break
                        except ValueError:
                            print("You must use numbers")
                    if choice < len(province[numberP]["ballotL"]):
                        province[numberP]["ballotL"].pop(choice)
                        print("Successfully Deleted")
                        ans = input("Keep deleting?")
                        if ans == "y" or ans == "y":
                            modifyBallotL()

                        else:
                            modifyBallots()
                    else:
                        print("Invalid option")

                else:
                    print("Invalid option")
                    modifyBallotP()


            else:
                print("No legislative ballot in this province")
                modifyBallots()
        else:
            print("\n"*10)
            print("No provinces")
            modifyBallots()

    def modifyBallots():
        option= input("Which ballot you want to modify  (1)Presidential (2)Legislatives (3)Back ")
        if option == "1":
            modifyBallotP()
        elif option == "2":
            modifyBallotL()
        elif option == "3":
            mainBallots()
        else:
            print("Invalid option")
            modifyBallots()




    def createBallotL():
        partitiesBallotL = partities[:]
        if province != []:
            a = 0
            while a < len(province):
                print(str(a) + "-) " + str(province[a]["name"]))
                a += 1
            invalidOption = False

            while invalidOption == False:
                try:
                    provinceBallot = int(input("TO WHICH PROVINCE WISHES YOU TO CREATE THE LEGISLATIVE BALLOT"))
                    break
                except ValueError:
                    print("You must use numbers")
            if province[provinceBallot]["ballotL"] == []:
                partitiesSet = []
                option = True
                while option == True:
                    x = 0
                    if partitiesBallotL != []:
                        while x < len(partitiesBallotL):
                            print(str(x) + "-) " + str(partitiesBallotL[x]["Name"]))
                            x += 1
                        invalidParitie = False
                        while invalidParitie == False:
                            try:
                                addPartitie = int(input("Which partitie you want to add to the LEGISLATIVE BALLOT?\n"))
                                break
                            except ValueError:
                                print("You must use numbers")
                        if addPartitie < len(partitiesBallotL):
                            extract = partitiesBallotL.pop(addPartitie)
                            partitiesSet.append(extract)

                            choice = input("Keep adding? (Y/N)")
                            if choice == "y" or choice == "Y":
                                option = True
                            else:
                                province[provinceBallot]["ballotL"] = partitiesSet
                                mainBallots()
                        else:
                            print("\n" * 10)
                            print("Invalid option")
                            createBallotL()
                    else:
                        print("\n" * 10)
                        print("All partities was added")
                        addBallots()


            else:
                print("\n" * 10)
                print("This province has a Legislative Ballot")
                addBallots()
        else:
            print("\n" * 10)
            print("No provinces")
            main()

    def deleteBallotP():
        if ballotP != []:
            print("Are you sure you want to delete the Presidential ballot?(Y/N)\n")
            if choice == "y" or choice == "Y":
                ballotP.clear()
            else:
                mainBallots()
        else:
            print("\n"*10)
            print("Presidential ballot doesnt exist")
            mainBallots()
    def deleteBallotL():
        a = 0
        while a < len(province):
            print(str(a) + "-) " + str(province[a]["name"]))
            a += 1
        invalidNumber=False
        while invalidNumber == False:
            try:
                numberP= int(input("From which province you want to delete the Legislative ballot?\n #Province"))
                break
            except ValueError:
                print("You must use numbers")
        if province[numberP]["ballotL"] !=[]:
            choice= input("Are you sure you want to delete the Legislative ballot from "+ str(province[numberP]["name"])+"?(Y/N)\n")
            if choice == "y" or choice == "Y":
                province[numberP]["ballotL"].clear()
                mainBallots()
            else:
                mainBallots()
        else:
            print("No Legislative ballot in this province")
            deleteBallots()

    def deleteBallots():
        choice = input("What ballot you want to delete (1)Presidential Ballot   (2)Legislative Ballot   (3)Back")
        if choice == "1":
            deleteBallotP()
        elif choice == "2":
            deleteBallotL()
        elif choice == "3":
            mainBallots()
        else:
            print("\n"*10)
            print("Invalid value")
            deleteBallots()





    #MAINBALLOTS STAR MENU
    if partities == []:
        print("No partities to add ballots")
        main()
    else:
        def addBallots():
            choice = input("Which ballot you want to create\n(1)Presidential ballot   (2)Legislative ballot     (3)Back\n")
            if choice == "1":#PRESIDENTIAL BALLOT
                createBallotP()

            elif choice == "2": #Legislative Ballot
                createBallotL()
            elif choice == "3":
                mainBallots()

            else:
                print("Invalid option")
                addBallots()


        print("Welcome to the ballots manager")
        choice= input("What do you want to do? \n (1)Add ballotts   (2)Modify ballots   (3)Delete ballots   (4)Main Page")
        if choice == "1":
            addBallots()
        elif choice == "2":
            modifyBallots()
        elif choice  == "3":
            deleteBallots()
        elif choice == "4":
            adminMenu()
        else:
            print("\n"*10)
            print("Invalid option")
            mainBallots()

def resultsMenu():
    choice = input("Select a Ballott \n (1)Presidential Ballott   (2)Legislative ballot   (3)Back")
    if choice == "1":
        print("\n" * 10)
        resultsP()
    elif choice == "2":
        print("\n"*10)
        resultsL()
    elif choice == "3":
        print("\n"*10)
        adminMenu()

def resultsP():
    if ballotP == []:
        print("\n"*10)
        print("No have Presidential Ballott")
        adminMenu()
    provinceStr = ""
    i = 0
    while i < len(province):
        provinceStr = provinceStr + "(" + str(i) + ")" + province[i]["name"] + " "
        i += 1
    print("Select a province")
    invalidOption = False
    while invalidOption == False:
        try:
            choice = int((input(provinceStr + " " + "(" + str(len(province)) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    invalidOption = False
    cantonStr = ""
    i = 0
    while i < len(province[choice]["cantons"]):
        cantonStr = cantonStr + "(" + str(i) + ")" + province[choice]["cantons"][i]["name"] + " "
        i += 1
    print("Select a canton")
    while invalidOption == False:
        try:
            choiceC = int((input(cantonStr + " " + "(" + str(len(province[choice]["cantons"])) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    invalidOption = False
    ditrictStr = ""
    i = 0
    while i < len(province[choice]["cantons"][choiceC]["districts"]):
        ditrictStr = ditrictStr + "(" + str(i) + ")" + province[choice]["cantons"][choiceC]["districts"][i]["name"] + " "
        i += 1
    print("Select a district")
    while invalidOption == False:
        try:
            choiceD = int((input(ditrictStr + " " + "(" + str(len(province[choice]["cantons"][choiceC]["districts"])) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    partiesStr = ""
    i = 0
    while i < len(ballotP):
        partiesStr = partiesStr + "(" + str(i) + ")" + ballotP[i]["Name"] + " "
        i += 1
    print("Select a partie")
    while invalidOption == False:
        try:
            choiceP = int((input(partiesStr + " " + "(" + str(len(ballotP)) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    districts = []
    while invalidOption == False:
        try:
            votos = int(input("How many votes for this partie: "))
            break
        except ValueError:
            print("You must use numbers")
    newV = {"District": province[choice]["cantons"][choiceC]["districts"][choiceD], "Votes": votos}
    districts.append(newV)
    ballotP[choiceP]["Votes"] = votos
    resultsMenu()

def resultsL():
    if province == []:
        print("\n" * 10)
        print("No have Presidential Ballott")
        adminMenu()
    provinceStr = ""
    i = 0
    while i < len(province):
        provinceStr = provinceStr + "(" + str(i) + ")" + province[i]["name"] + " "
        i += 1
    print("Select a province")
    invalidOption = False
    while invalidOption == False:
        try:
            choice = int((input(provinceStr + " " + "(" + str(len(province)) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    invalidOption = False
    cantonStr = ""
    i = 0
    while i < len(province[choice]["cantons"]):
        cantonStr = cantonStr + "(" + str(i) + ")" + province[choice]["cantons"][i]["name"] + " "
        i += 1
    print("Select a canton")
    while invalidOption == False:
        try:
            choiceC = int((input(cantonStr + " " + "(" + str(len(province[choice]["cantons"])) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    invalidOption = False
    ditrictStr = ""
    i = 0
    while i < len(province[choice]["cantons"][choiceC]["districts"]):
        ditrictStr = ditrictStr + "(" + str(i) + ")" + province[choice]["cantons"][choiceC]["districts"][i]["name"] + " "
        i += 1
    print("Select a district")
    while invalidOption == False:
        try:
            choiceD = int((input(ditrictStr + " " + "(" + str(len(province[choice]["cantons"][choiceC]["districts"])) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    partiesStr = ""
    i = 0
    if province[choice]["ballotL"] == []:
        print("No have ballot in this province")
        resultsP()
    while i < len(province[choice]["ballotL"]):
        partiesStr = partiesStr + "(" + str(i) + ")" + province[choice]["ballotL"][i]["Name"] + " "
        i += 1
    print("Select a partie")
    while invalidOption == False:
        try:
            choiceP = int((input(partiesStr + " " + "(" + str(len(province[choice]["ballotL"])) + ")" + "Back" + "\n")))
            break
        except ValueError:
            print("You must use numbers")
    districts = []
    while invalidOption == False:
        try:
            votos = int(input("How many votes for this partie: "))
            break
        except ValueError:
            print("You must use numbers")
    newV = {"District": province[choice]["cantons"][choiceC]["districts"][choiceD], "Votes": votos}
    districts.append(newV)
    province[choice]["ballotL"][choiceP]["Votes"] = votos
    resultsMenu()

def queries():
    invalidOption = False
    while invalidOption == False:
        try:
            choiceP = int(input("1)National 2)Provincial 4)Cantonal 3)District 5)Back"))
            break
        except ValueError:
            print("You must use numbers")
    if choiceP == "3":
        provinceStr = ""
        i = 0
        while i < len(province):
            provinceStr = provinceStr + "(" + str(i) + ")" + province[i]["name"] + " "
            i += 1
        print("Select a province")
        invalidOption = False
        while invalidOption == False:
            try:
                choice = int((input(provinceStr + " " + "(" + str(len(province)) + ")" + "Back" + "\n")))
                break
            except ValueError:
                print("You must use numbers")
        invalidOption = False
        cantonStr = ""
        i = 0
        while i < len(province[choice]["cantons"]):
            cantonStr = cantonStr + "(" + str(i) + ")" + province[choice]["cantons"][i]["name"] + " "
            i += 1
        print("Select a canton")
        while invalidOption == False:
            try:
                choiceC = int((input(cantonStr + " " + "(" + str(len(province[choice]["cantons"])) + ")" + "Back" + "\n")))
                break
            except ValueError:
                print("You must use numbers")
        invalidOption = False
        ditrictStr = ""
        i = 0
        while i < len(province[choice]["cantons"][choiceC]["districts"]):
            ditrictStr = ditrictStr + "(" + str(i) + ")" + province[choice]["cantons"][choiceC]["districts"][i][
                "name"] + " "
            i += 1
        print("Select a district")
        while invalidOption == False:
            try:
                choiceD = int((input(ditrictStr + " " + "(" + str(
                    len(province[choice]["cantons"][choiceC]["districts"])) + ")" + "Back" + "\n")))
                break
            except ValueError:
                print("You must use numbers")
        i = 0
        while i < len(province[choice]["cantons"][choiceC]["districts"][choiceD]["ballots"]):
            name = (province[choice]["cantons"][choiceC]["districts"][choiceD]["ballots"][i]["Name"])
            vote = (province[choice]["cantons"][choiceC]["districts"][choiceD]["ballots"][i]["Votes"])
            print(str(name) + " " + str(vote))
            i += 1
    elif choiceP == "5":
        adminMenu()
    else:
        queries()


main()