from random import randint            #for transaction id generation
#Home page
def home():
    print("-----------------Welcome to ABC Mart--------------")
    print("Log in to proceed")
    print("1.Customer \n2.Admin")
    choice=input("Enter the choice:")
    return choice

#User and admin list, instead of database
usrlist=["abinaya","nithilan","selvakumar","santhi","kandasamy","kavusalya"]
admlist=["admin1","admin2","admin3"]

#login for user and admin
def log_in(name,pwd,mode):
    if mode=="user":
        if name in usrlist and pwd=='123':
            print(name,"logged in successfully!")
            return True
        else:
            print("Entered user not in the list")
            return False
    elif mode=="admin":
        if name in admlist and pwd=='456':
            print(name,"logged in successfully")
            return True
        else:
            print("Entered admin not in the list")
            return False
    else:
        print("Incorrect username or password!")
        return False  

#check the product availablility
def check(pro,li):
    count=0
    for p in li:
        if p[0]==pro:
            print(p[0],count)
            yield True
            yield count      
        count+=1 
        yield 0  

#adding product in the particular category                         
def add_product(pro,pri,li):
    li1=[pro,pri]
    var=check(pro,li)
    if next(var)==True:
        li[next(var)]=[pro,pri]    
    else:    
        li.append(li1)
    print("Product has been added to the store")
    return li

#Removing products whenever not avilable
def remove_product(name,li):
    for p in li:
        if p[0]==name:
            li.remove(p)
    print("Product has been removed from the store")   
    return li   

#displaying products
def display(li):
    print("Product --------------------Price")
    for p in li:
        print(f'{p[0]}               {p[1]}')

#customer cart       
class shopping_cart:
    cart=[]
    def __init__(self,li):
        self.li=li
     
    def add_to_cart(self,product,quantity):

        for p in self.li:
            if p[0]==product:
                shopping_cart.cart.append([product,p[1],quantity])
                print("added to the cart")       
                break                      
    
    def bill(self):
        print("Product(Quantity)----------------Price" )
        for p in shopping_cart.cart:
            print(f'{p[0]}({p[2]})               ',int(p[1]*p[2]))
        total=0
        for p in shopping_cart.cart:
            total=total+(int(p[1])*int(p[2]))
        print("----------------------------------------------")    
        print(f'Total:                         Rs.',total)     
        print("----------------------------------------------")
           
    def display_cart(self):
        print("Product----------------Quantity" )
        for p in shopping_cart.cart:
            print(f'{p[0]}                   {p[2]}')
    
    def logout(self): 
       print("logged out successfully")
       shopping_cart.cart=[]
    
    def payment(self,card,otp):
        if card=='1234 4567 8910' and otp=='778899':
            print("payment successful! ")
            print("Transaction ID:TRANID",randint(100000,999999))
            return 1
        else:
            print("payment unsuccessful! Try again")
            return 0
                
    def category(self,li_g,li_mo,li_cl):
        print("CATEGORIES:-")
        print("1.Grocery\n2.Mobiles\n3.cloths")
        while True:
            cat=input("Enter Category to purchase:")
            if cat=='1':
                self.li=li_g
                for i in self.li:
                    print(f'{i[0]}        Rs.{i[1]}')              
                return self.li 
            elif cat=='2':
                self.li=li_mo
                for i in self.li:
                    print(f'{i[0]}        Rs.{i[1]}')               
                return self.li
            elif cat=='3':
                self.li=li_cl
                for i in self.li:
                    print(f'{i[0]}        Rs.{i[1]}')
                return self.li
            else:
                print("Enter correct category")
                continue

