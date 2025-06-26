from flask import Flask,render_template,request,redirect,url_for,jsonify
import mysql.connector
from mysql.connector import Error
market=Flask(__name__)
# MySQL connection configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Abinaya@123',
    'database': 'super_market'
}

@market.route('/',methods=["GET","POST"])
def home():
    return render_template("Home.html")

@market.route('/signup',methods=["GET","POST"])
def reg():
        if request.method == 'POST':
            fname = request.form.get('firstname')
            lname = request.form.get('lastname')
            age = request.form.get('age')
            mobile= request.form.get('mobile') 
            email = request.form.get('email')
            password = request.form.get('password')
            
        # Establishing a connection to MySQL database
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()
            
            cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INT AUTO_INCREMENT PRIMARY KEY,
                fname VARCHAR(50) NOT NULL,
                lname VARCHAR(50) NOT NULL,                
                age INT,mobile INT,email VARCHAR(255),
                password VARCHAR(50)               
            )''')
        # Inserting data into the MySQL database
            cur.execute("INSERT INTO users(fname,lname,age,mobile,email,password) VALUES (%s,%s,%s,%s,%s,%s)",
                     (fname,lname,age,mobile,email,password))
            con.commit()
            con.close()
        
            return '<h4>Registered successfully</h4>'
        else:
            return render_template("registration.html")


@market.route('/check',methods=["GET","POST"])
def check():
    if request.method=='POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()
            cur.execute("Select id,fname from users where email=(%s) and password=(%s)",(email,password))
            result=cur.fetchone()
            if result:
                user_id, name = result
                designation="user"
                return render_template("userprof.html", id=user_id, name=name,designation=designation)
            else:
                return "Invalid credentials, please try again."
        except Error as e:
            return f"An error occurred: {e}"
        finally:
            if con.is_connected():
                cur.close()
                con.close()
            else:
                pass
    else:
        return render_template("logn.html")
    

@market.route('/all_user',methods=["POST"])
def alluser():
        
        con = mysql.connector.connect(**mysql_config)
        cur = con.cursor()
        cur.execute('''Select * from users''')
        us_list=cur.fetchall()
        cur.close()
        return jsonify((us_list))

@market.route('/store_user/registration',methods=["GET","POST"])
def store_table():
        if request.method == 'POST':
            empid = request.form.get('id')
            fname = request.form.get('firstname')
            lname = request.form.get('lastname')
            age = request.form.get('age')
            sex=request.form.get('sex')
            mobile= request.form.get('mobile') 
            email = request.form.get('email')
            password = request.form.get('password')
            designation=request.form.get('designation')
            
            # Estabilishing a connection to MySQL database
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()
            
            cur.execute('''CREATE TABLE IF NOT EXISTS Store_users(
                empid VARCHAR(11) PRIMARY KEY,
                fname VARCHAR(50) NOT NULL,
                lname VARCHAR(50) NOT NULL,                
                age INT,sex VARCHAR(10),mobile INT,email VARCHAR(255),
                password VARCHAR(50),designation VARCHAR(15)               
            )''')
            # Inserting data into the MySQL database
            
            cur.execute("INSERT INTO store_users(empid,fname,lname,age,sex,mobile,email,password,designation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                     (empid,fname,lname,age,sex,mobile,email,password,designation))
            con.commit()
            con.close()
        
            return f'<h4>Store User {fname} Registered successfully</h4>'
        else:
            return render_template("storeuser.html")

@market.route('/store_user/login',methods=["GET","POST"])
def slogin():
    if request.method=='POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            designation=request.form.get('designation')
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()
            cur.execute("Select empid,fname,designation from Store_users where email=(%s) and password=(%s) and designation=(%s)",(email,password,designation))
            result=cur.fetchone()
            print(result)
            if result:
                user_id, name, designation = result
                return render_template("userprof.html", id=user_id, name=name,designation=designation)
            else:
                return "Invalid credentials, please try again."
        except Error as e:
            return f"An error occurred: {e}"
        finally:
            if con.is_connected():
                cur.close()
                con.close()
            else:
                pass
    else:
        return render_template("storelogin.html")
   
@market.route('/products/<choose>',methods=["GET","POST"])
def product_add(choose):
    if request.method=="POST":
        if choose=="add":
            Product_id=request.form.get('productid')
            Product_name=request.form.get('productname')
            Rate=request.form.get('price')
            Stock=request.form.get('quantity')
            # Establishing a connection to MySQL database
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()         
            cur.execute('''CREATE TABLE IF NOT EXISTS products(
                Product_id VARCHAR(11) PRIMARY KEY,
                Product_name VARCHAR(50) NOT NULL,
                Rate VARCHAR(50) NOT NULL,                                
                Stock VARCHAR(50)               
                )''')
            # Inserting data into the MySQL database
            cur.execute("INSERT INTO products(Product_id,Product_name,Rate,Stock) VALUES (%s,%s,%s,%s)",
                     (Product_id,Product_name,Rate,Stock))
            con.commit()
            return f'<p>{Product_name} added successfully</p>'
        elif choose=="delete":
            Product_id=request.form.get('productid')
            Product_name=request.form.get('productname')
            # Establishing a connection to MySQL database
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()
            cur.execute("DELETE FROM products WHERE Product_id=(%s) and Product_name=(%s)",
                     (Product_id,Product_name))
            con.commit()
            return f'<p>{Product_name} removed successfully</p>'
        elif choose=="update":
            Product_id=request.form.get('productid')
            Product_name=request.form.get('productname')
            Rate=request.form.get('price')
            # Establishing a connection to MySQL database
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()
            cur.execute("UPDATE products SET Rate=(%s) WHERE Product_id=(%s) and Product_name=(%s) ",
                     (Rate,Product_id,Product_name))
            con.commit()
            return f'<p>{Product_name} price updated successfully</p>'
        else:
            return f'<p>Choose mode</p>'
    else:
        return render_template("products.html",choose=choose)
        
@market.route('/purchase/<id>/<name>/<designation>',methods=["GET","POST"])
def purchase_entry(id,name,designation):
    if request.method=='POST':
        user_id=id
        Product_name=request.form.get('productname')
        quantity=request.form.get('quantity')        
        con = mysql.connector.connect(**mysql_config)
        cur = con.cursor()         
        cur.execute('''CREATE TABLE IF NOT EXISTS purchase_entry(
                User_id VARCHAR(11) NOT NULL,
                Product_name VARCHAR(50) NOT NULL,
                Quantity INT NOT NULL,                                
                Rate INT,Date DATE             
            )''')
        
        # Inserting data into the MySQL database
        cur.execute("Select fname from users where id=(%s)",(user_id,))
        name=cur.fetchone()
        name=name[0].lower()        
        cur.execute("SELECT Rate from products where Product_name=(%s)",(Product_name,))
        price=cur.fetchone()
        Rate=price[0] 
        total=int(Rate)*int(quantity)
        cur.execute("INSERT INTO purchase_entry(User_id,Product_name,Quantity,Rate,Date) VALUES (%s,%s,%s,%s,CURDATE())",
                     (user_id,Product_name,quantity,total))
        con.commit()
        return render_template("userprof.html", id=user_id, name=name,designation=designation)
    else:
        return render_template("purchase.html",id=id,name=name,designation=designation)

@market.route('/reports/<var>',methods=["GET","POST"])
def report(var):
    if request.method=="POST":
        if var=='date_between':
            start_date=request.form.get('start_date')
            end_date=request.form.get('end_date')
            print(start_date)
            con = mysql.connector.connect(**mysql_config)
            cur = con.cursor()

            cur.execute('''select Product_name,sum(Quantity) as num_of_items_in_kg from purchase_entry 
                        where Date between (%s) and (%s) group by Product_name ''',(start_date,end_date))
            result=cur.fetchall()
            cur.close()
            con.close()
            return result
        elif var=='dropdown':
            option=request.form.get('dropdown')
            if option=="high_purchase":
                con = mysql.connector.connect(**mysql_config)
                cur = con.cursor()
                cur.execute('''select User_id,sum(Rate) as amount from purchase_entry 
                            where Date=current_date() group by User_id having amount>=1000 ''')
                result=cur.fetchall()
                cur.close()
                con.close()
                return result
                                
            elif option=="shampoo":
                con = mysql.connector.connect(**mysql_config)
                cur = con.cursor()
                cur.execute('''select Product_name,sum(quantity) as no_of_packets,sum(Rate) as totalsales from purchase_entry 
                            where Product_name="Tomato" AND Date >= CURDATE() - INTERVAL 7 DAY ''')
                result=cur.fetchall()
                cur.close()
                con.close()
                return result
        else:
            return f'Enter Valid response'    
     
    else:
        return render_template("reports.html",var='none')
if __name__=="__main__":
    market.run(debug=True)
