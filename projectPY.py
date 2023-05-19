import os


# define a class
class DeliveryBoy:
    DeliveryBoyName = ""
    PhoneNumber = ""
    AreaCode = ""
    Login_username = ""


class CustomerSignup:
    user_name = ""
    password = ""
    areacode = ""
    phone = ""

class TakeOrder:
    order=""
    customerName=""
    areacode=""
    customerPhone=""
    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def encrypt(s):
    s2 = ""
    for x in s:
        x = chr(ord(x) + 6)
        s2 = s2 + x
    s = s2


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def decrypt(s):
    s2 = ""
    for x in s:
        x = chr(ord(x) - 6)
        s2 = s2 + x
    s = s2


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Adding new customer in file

def signup():  # signup
    try:

        fileOrder=open("TakeOrder.txt","w")
        with open("Login.txt", "a") as file:
            obj = CustomerSignup()
            obj.user_name = input('Please, Enter Your User Name : ')
            obj.password = input('Please, Enter Your Password : ')
            encrypt(obj.password)
            obj.phone = input('Please, Enter Your Phone Number : ')
            obj.areacode = input('Please, Enter Your Area code : ')
            obj2=TakeOrder()
            obj2.order=input("Please ,Enter \"Yes\" if you want Make order other than that Enter \"No\" :")
            if obj2.order=="Yes":
                obj2.customerName=obj.user_name
                obj2.areacode=obj.areacode
                obj2.customerPhone=obj.phone
                fileOrder.write(obj2.customerName+'\t'+obj2.customerPhone+'\t'+obj2.areacode+'\t \n')
            file.write(obj.user_name + '\t' + obj.password + '\t' + obj.phone + '\t' + obj.areacode + '\t \n')
        print("\n-----------Welcome :)---------- \n")
        return True
    except IOError:
        print("Bad , File not Found :(")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# display Records for "ADMIN" only

def detailCustomer():
    try:
        with open("TakeOrder.txt", "r") as file:
            print("**************************(: detail Customer :)***************************")
            for line in file:
                    x=line.split('\t')
                    print("User_name : ",x[0])
                    print("Phone Number : ",x[1])
                    print("Area code : ",x[2])
                   
                    
                    SearchDeliveryboy(x[2])
    except IOError:

        print("Bad , File not Found :(")

def disPlayAllCustomer():
    try:

        with open("Login.txt", "r") as file:
            isTrue = False
            password = input("Please ,Enter The  Admin Password : ")
            if password == "Admin":
                isTrue = True
                print('user_name\tpassword\tphone\tareacode')
                print('----------------------------------------------------')
                for line in file:
                    print(line)
        if not isTrue:
            print("Sorry Wrong Password , cannot do this function :(")

    except IOError:

        print("Bad , File not Found :(")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#   search for a ("signin customer") in SignUp data by username & password

def signin():
    obj = CustomerSignup()
    obj2=TakeOrder()
    try:
        fileOrder=open("TakeOrder.txt","w")

        with open("Login.txt", "r") as file:
            isValid_login = False
            user_name = input('Please, Enter Your User Name : ')
            password = input('Please, Enter Your Password : ')
            
            decrypt(obj.password)
            for line in file:
                records = line.split('\t')
                if user_name == records[0] and password == records[1]:
                    isValid_login = True
                    obj2.customerName=records[0]
                    obj2.areacode=records[3]
                    obj2.customerPhone=records[2]
        if isValid_login:
            print("\nWelcome , Login Successful :) \n")
            
            obj2.order=input("Please ,Enter \"Yes\" if you want Make order other than that Enter \"No\" :")
            if obj2.order=="Yes":
                fileOrder.write(obj2.customerName+'\t'+obj2.customerPhone+'\t'+obj2.areacode+'\t \n')
            return True
        else:
            print("\nwrong password or username :( \n1.signin \t 2.signup\n ")
            x=input("Enter your choice : ")
            if x=='1':
                return  signin()
            elif x=='2':
                return signup()
            else :
                return False
    except IOError:
        print("Bad , File not Found :(")


# delete customer
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def logout():
    
    obj = CustomerSignup()
    #disPlayAllCustomer()
    try:
        
        file = open("Login.txt", "r")
        TempFile = open("TempFile.txt", "a")
        password = input('Please, Enter Your Password : ')
        Flag = False
        for line in file:
            records = line.split('\t')

            if records[1] == password:
                Flag = True

            else:
                TempFile.write(line)

        file.close()
        TempFile.close()
        os.remove("Login.txt")
        os.rename("TempFile.txt", "Login.txt")
        if Flag:
            print("logout Successful\n")
           # disPlayAllCustomer()
        else:
            print("wrong password\n")
    except IOError:
        print("Bad , File not Found :(")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Reset 'password'
# username static

def updatepassword():
    
    obj = CustomerSignup()
    try:

        file = open("Login.txt", "r")
        tempFile = open('TempFile.txt', 'a')
        old_password = input("Please , Enter Your Old Password : ")
        decrypt(obj.password)
        flag = False
        for line in file:
            records = line.split('\t')
            if old_password == records[1]:
                flag = True
                new_password = input("Please , Enter Your New Password : ")
                line = records[0] + '\t' + new_password + '\t' + records[2] + '\t' + records[3] 
            tempFile.write(line)
        file.close()
        tempFile.close()

        os.remove("Login.txt")
        os.rename("TempFile.txt", "Login.txt")

        if not flag:
            print("Incorrect password, please try again. :(\n")
        else:
            print("Great! Password Updated")
    except IOError:
        print("Bad , File not Found :(")


# Adding New Record in Delivery Boy  
def AddDeliveryBoy():
    c = 'y'
    obj = DeliveryBoy()
    try:
        with  open('DeliveryBoy.txt', 'a') as file:
            while c == 'y':
                obj.AreaCode = input('Enter Area Code for Delivery Boy : ')
                obj.DeliveryBoyName = input('Enter Name for Delivery Boy : ')
                obj.PhoneNumber = input('Enter Phone Number for Delivery Boy : ')
                obj.Login_username = input('Enter username for Delivery Boy : ')
                encrypt(obj.Login_username)

                c = input('Enter record agin(y/n) ')
                file.write( obj.AreaCode + '\t' + obj.DeliveryBoyName + '\t' + obj.PhoneNumber + '\t' + obj.Login_username + '\n')
    except IOError:
        print('Cannot open file :( ')


# Display All Deliveryboys
def dispalyALLDeliveryboys():
    obj = DeliveryBoy()
    try:
        with  open('DeliveryBoy.txt', 'r') as file:
            print('AreaCode |Name |PhoneNumber |Login_username ')
            print('----------------------------------------------------')
            for line in file:
                decrypt(obj.Login_username)
                print(line, end='')
    except IOError:
        print('Cannot open the specified file :( ')


# search for Deliveryboy by area code       
def SearchDeliveryboy(str):
    obj = DeliveryBoy()
    try:
        #str = input('Enter Area code search Record : ')
        with  open('DeliveryBoy.txt', 'r') as file:
            flag = False
            for line in file:
                fields = line.split('\t')
                if fields[0] == str:
                    flag = True
                    print("**************************(: detail Delivery Boy :)***************************")
                    decrypt(obj.Login_username)
                    
                    x=line.split('\t')
                    print("Name : ",x[1])
                    print("Phone Number : ",x[2])
                    print("Area Code : ",x[0])


            if not flag:
                print('not found :( ')
    except IOError:
        print('cannot open the specified file.')


# Delete Record
def DeleteDeliveryboy():
    import os
    dispalyALLDeliveryboys()
    try:
        file = open('DeliveryBoy.txt', 'r')
        tempFile = open('tempDeliveryBoy.txt', 'w')
        str = input('Enter Name DeliveryBoy to delete his record : ')
        flag = False
        for line in file:
            fields = line.split('\t')
            if fields[1] == str:
                flag = True
            else:
                tempFile.write(line)
        file.close()
        tempFile.close()
        os.remove('DeliveryBoy.txt')
        os.rename('tempDeliveryBoy.txt', 'DeliveryBoy.txt')

        if not flag:
            print('DeliveryBoy not found')
        else:
            print('DeliveryBoy deleted successfully')
            dispalyALLDeliveryboys()
    except IOError:
        print('cannot open the specified file.')


# Update Phone of Deliveryboy
def UpdateDeliveryboy():
    import os
    obj = DeliveryBoy()
    dispalyALLDeliveryboys()
    try:
        file = open('DeliveryBoy.txt', 'r')
        tempFile = open('tempDeliveryBoy.txt', 'w')
        str = input('Enter name Delivery Boy to udate for : ')
        flag = False
        for line in file:
            fields = line.split('\t')
            if fields[1] == str:
                flag = True

                obj.PhoneNumber = input('Enter the new Phone Number for Delivery Boy  :')

                line = fields[0] + '\t' + fields[1] + '\t' + obj.PhoneNumber + '\t' + fields[3]

            tempFile.write(line)
        file.close()
        tempFile.close()
        os.remove('DeliveryBoy.txt')
        os.rename('tempDeliveryBoy.txt', 'DeliveryBoy.txt')

        if not flag:
            print('DeliveryBoy not found')
        else:
            print('DeliveryBoy update successfully')
            dispalyALLDeliveryboys()
    except IOError:
        print('cannot open the specified file.')


##----Size of string----
def sz(s):
    count = int(0)
    for ch in s:
        count += 1
    return count


##----Record Data----
def writeMenue():
    try:
        with open("menue.txt", "a") as file :
            c="y"
            while c == "y":
                id = input("Enter item ID : ")
                type = input("Enter the item type : ")
                charge = input("Enter charge of item : ")
                file.write(id + "\t" + type + "\t" + charge + "\n")
                c = input("do you want to enter record again (y/n)? ")
    except IOError:
        print("File not Found")

##----Read Data----
def readMenue():
    try:
        with open("menue.txt","r") as file:
            print("ID\tType\tCharge\t")
            print("-----------------------")
            for line in file:
              print(line, end="")
    except IOError:
        print("File not Found")

##----search item with id----
def searchMenue():
    try:
        id = input("Enter a Id of Type to search for? ") 
        with open("menue.txt", "r") as file:     
           flag = False
           for line in file:
               fields = line.split("\t")
               if fields[0] == id:
                   flag = True
                   print("ID\tType\tCharge\t")
                   print("------------------------")
                   print(line)
                   
        if not flag:
            print("Type with this id not found")
    except IOError: 
        print("not Found")



def chargeItem(item):
    try:   
        with open("menue.txt", "r") as file:
            
            flag = False
            for line in file:
                fields = line.split("\t")
                if fields[1] == item:
                    return fields[2][0:sz(fields[2]) - 1]
        if not flag:
            return -1
    except IOError:
        print("not Found")
##----update item's charge----
def updateMenue():
    import os
    try:
        id = input("Enter Id of Type to update :")
        file = open("menue.txt", "r")
        tempFile = open("copyMenue.txt", "a")
        flag = False
        for line in file:
            st = line.split("\t")
            if st[0] == id:
                flag = True
                charge = input("Enter the new Charge for item " + st[1]+" ")
                line = st[0] + "\t" + st[1] + "\t" + charge + "\n"
            tempFile.write(line)
        file.close()
        tempFile.close()
        os.remove("menue.txt")  # deleted original file
        os.rename("copyMenue.txt", "menue.txt")  # rename temp file
        if flag:
            print("charge Type Updated")
        else:
            print("Type with this id not found")
    except IOError:
        print("not Found")

##----Delete item with id----

def deletefromMenue():
    import os
    try:   
        id = input("Enter id of the item to delete :")
        file = open("menue.txt", "r")
        tempFile = open("copyMenue.txt", "a")
        flag = False
        for line in file:
            fields = line.split("\t")
            if fields[0] == id:
                flag = True
            else:
                tempFile.write(line)
        file.close()
        tempFile.close()
        os.remove("menue.txt")
        os.rename("copyMenue.txt", "menue.txt")
        if not flag:
            print("Type with this id not found")
        else:
            print("Type deleted")
    except IOError:
        print("not Found")
##------Discounts----------------------------------------------------------------##
def addDiscount():
    with open ('DsicountsPy.txt','a') as file:
        c='y'
        while c=='y':
            discount_id=input('Enter the discount ID: ')
            product_name=input('Enter the name of the product: ')
            start_date=input('Enter the start date: ')
            end_date=input('Enter the expire date: ')
            discount_amount=int(input('Enter the amount of discount: '))
            original_price=int(input('Entre the original price: '))
            final_price=int(original_price)-((int(discount_amount)/100)*int(original_price))
            file.write(discount_id+'\t'+product_name+'\t'+start_date+'\t'+end_date+'\t'+str(discount_amount)+'\t'+str(original_price)+'\t'+str(final_price)+'\n')
            c=input('sir!, Do You want to add more discounts! (y/n)')
        print('Items Added successfully! :)')
        
##display all discounts 
def displayDiscounts():
    with open ('DsicountsPy.txt','r') as file:
        print ('discount_id\tproduct_name\tstart_date\tend_date\tdiscount_amount\toriginal price\tprice_after_discount')
        print ("------------------------------------------------------------------------------------------")
        
        for line in file :
            print(line,end="")
            
##search for discounts
def searchDiscounts():
    name=input('Enter the name of the product to search discount!')
    flage=False
    with open ('DsicountsPy.txt','r') as file:
        for line in file :
            fields=line.split('\t')
            if fields[1]==name:
                flage=True
                print(line,end='\n')
        if (not flage):
            print('No discounts avaliable, Sir!') 
##delete a discount 
def deleteDiscount():
    import os
    flage=False
    id =input ('Entre the id of the discount to delete it!')
    file=open ('DsicountsPy.txt','r')
    temp=open('temp.txt','w')
    for line in file :
            fields=line.split('\t')
            if fields[0] == id:
                flage=True
            else:
                temp.write(line)
    file.close()
    temp.close()
    os.remove('DsicountsPy.txt')
    os.rename('temp.txt','DsicountsPy.txt')
    if not flage:
        print ('there is no discounts with that ID to delet')
    else:
        print ('item deleted!')

##update on discount
def updateDiscount():
    import os
    flage=False
    id =input ('Entre the id of the discount to update it!')
    file=open ('DsicountsPy.txt','r')
    temp=open('temp.txt','w')
    for line in file :
            f=line.split('\t')
            if f[0] == id:
                flage=True
                newDiscount=input('Entre the new discount for : '+f[1]+' ')
                final_price=int(f[5])-((int(newDiscount)/100)*int(f[5]))
                line= f[0]+'\t'+f[1]+'\t'+f[2]+'\t'+f[3]+'\t'+newDiscount+'\t'+f[5]+'\t'+str(final_price)+'\n'
            temp.write(line)
    file.close()
    temp.close()
    os.remove('DsicountsPy.txt')
    os.rename('temp.txt','DsicountsPy.txt')
    if not flage:
        print ('there is no discounts with that ID to delet')
    else:
        print ('item updated!')
        
    ##-------------------------------------------------------------------------

    ##----Total price----


##write
def readTotalPrice():
    try:
        with open("TotalPrice.txt", 'r') as price:
            return price.read()
    except IOError:
        print('cannot open the specified file.')


##read
def writeTotalPrice(x):
    try:
        with open("TotalPrice.txt", 'w') as price:
            price.write(str(x))
    except IOError:
        print('cannot open the specified file.')


##----Make order---- 

def MakeOrder():
    import os
    try:
        os.remove("Order.txt")
    except IOError:
        print("-----Welcome-----)")
    try:
      if(signin()):
        TotalPrice = int(0)
        with open("Order.txt", 'a') as file:
            c = 'y'
            while c == 'y':
                readMenue()
                item = input("\nEnter type of item : ")
                charge = chargeItem(item)
                if charge == -1:
                    print("Not found in Menue :( ")
                else:
                    amount = input("Enter amount : ")
                    TotalCharge = str(int(charge) * int(amount))
                    TotalPrice += int(TotalCharge)
                    file.write(item + '\t' + amount + '\t' + charge + '\t' + TotalCharge + '\n')
                c = input("\nBuy other item (y/n) ? ")

            writeTotalPrice(TotalPrice)
      else:
        print('To Make Order you should signup !!')
    except IOError:
        print('cannot open the specified file.')


##----add item order---- 
def AddItemInorder():
    try:
        with open("Order.txt", 'a') as file:
            TotalPrice = int(readTotalPrice())

            c = 'y'
            while c == 'y':
                readMenue()
                item = input("\nEnter type of item : ")
                charge = chargeItem(item)
                if charge == -1:
                    print("Not found in Menue :( ")
                else:
                    amount = input("Enter amount : ")
                    TotalCharge = str(int(charge) * int(amount))

                    TotalPrice += int(TotalCharge)

                    file.write(item + '\t' + amount + '\t' + charge + '\t' + TotalCharge + '\n')
                c = input("\nBuy other item (y/n) ? ")
            writeTotalPrice(TotalPrice)
           
    except IOError:
        print('cannot open the specified file.')


##----Read order----
def ReadOrder():
    try:

        with open("Order.txt", 'r') as file:
            print("Item\tAmount\tCharge\tTotalCharge")
            print("---------------------------------------------------")
            for line in file:
                print(line, end="")

            print("Total Price : ", readTotalPrice())

    except IOError:
        print("You do not make order !!")

    ##---search of item in order----


def SearchInOrder():
    try:
        with open("Order.txt", 'r') as file:
            item = input("Enter item : ")
            found = False
            for line in file:
                order = line.split('\t')
                if item == order[0]:
                    found = True
                    print("Item\tAmount\tCharge\tTotalCharge")
                    print("---------------------------------------------------")
                    print(line)
                    break
            if not found:
                print("You do not buy this item !!")
    except IOError:
        print("You do not make order !!")

    ##---Delete item from order----


def DeleteItemFromOrder():
    try:

        import os

        file = open("Order.txt", 'r')
        tempFile = open("TempOrder.txt", 'a')
        item = input("Enter item : ")
        TotalPrice = int(readTotalPrice())

        found = False
        for line in file:
            order = line.split('\t')
            if item != order[0]:
                tempFile.write(line)
            else:
                found = True
                TotalPrice -= int(order[3])

        if found:
            writeTotalPrice(TotalPrice)
            print("Deleted Successful :) ")

        else:
            print("You do not buy this item !!")
        file.close()
        tempFile.close()
        os.remove("Order.txt")
        os.rename("TempOrder.txt", "Order.txt")
    except IOError:
        print("You do not make order  !!")

    ##---update amount in order----


def UpdateAmountInOrder():
    try:

        import os

        file = open("Order.txt", 'r')
        tempFile = open("TempOrder.txt", 'a')
        item = input("Enter item : ")
        TotalPrice = int(readTotalPrice())

        found = False
        for line in file:
            order = line.split('\t')
            if item == order[0]:
                found = True
                TotalPrice -= int(order[3])
                amount = input("Enter new Amount : ")
                Totalcharge = str(int(amount) * int(order[2]))
                TotalPrice += int(Totalcharge)
                line = order[0] + '\t' + amount + '\t' + order[2] + '\t' + Totalcharge + '\n'

            tempFile.write(line)

        if found:
            writeTotalPrice(TotalPrice)
            print("Updated Successful :) ")
        else:
            print("You do not buy this item !!")
        file.close()
        tempFile.close()
        os.remove("Order.txt")
        os.rename("TempOrder.txt", "Order.txt")
    except IOError:
        print("You do not make order  !!")


def home():

    print('░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗██╗')
    print('░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝██║')
    print('░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░██║')
    print('░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░╚═╝')
    print('░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗██╗')
    print('░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝')
    
    c = "y"
    while c == "y":
        print("Enter 1 : to add new item to Menue")
        print("Enter 2 : to read all Menue ")
        print("Enter 3 : to search for type you need")
        print("Enter 4 : to update an item ")
        print("Enter 5 : to delete Menue")
        print("Enter 6 : to Make New order ")
        print("Enter 7 : to Display your order ")
        print("Enter 8 : to search for item in order")
        print("Enter 9 : to update amount of buyed item ")
        print("Enter 10: to delete item from your order ")
        print("Enter 11: to Add Item In your Order ")
        print("Enter 12: to Print Details Order ")
        #for discounts
        print("Enter 13: to Print all Discounts avaliable ")#need edit 
        print("Enter 14: to add discounts for menue items ")
        print("Enter 15: to check if a specific item has a discounts ") #need edit
        print("Enter 16: to delete a discount ")
        print("Enter 17: to update the value of a discount ")

        c = input("your choice: ")
        if c == "1":
            writeMenue()
        elif c == "2":
            readMenue()

        elif c == "3":
            searchMenue()
        elif c == "4":
            updateMenue()
        elif c == "5":
            deletefromMenue()
        elif c == "6":
            MakeOrder()
        elif c == "7":
            ReadOrder()
        elif c == "8":
            SearchInOrder()
        elif c == "9":
            UpdateAmountInOrder()
        elif c == "10":
            DeleteItemFromOrder()
        elif c == "11":
            AddItemInorder()
        elif c == "12":
            print("\n******************************(:  Details Order  :)**************************\n")
            ReadOrder()
            detailCustomer()
            
        elif c == "13":
            displayDiscounts()
        elif c == "14":
            addDiscount()
        elif c == "15":
            searchDiscounts()
        elif c == "16":
            deleteDiscount()
        elif c == "17":
            updateDiscount()
                   
        c = input("\nperform another operation (y/n): ")
home()