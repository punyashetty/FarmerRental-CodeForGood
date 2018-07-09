import MySQLdb

class MyDatabase:
    def __init__(self):
        self.db=MySQLdb.connect(host="localhost", user="root", passwd="root", db="EMPLOYEE")#connection object
        self.cur = self.db.cursor()#create cursor to point to records
		
    def insert(self, slno, name, address, empcode, dob, age, mobile, status, designation):
        self.cur.execute("INSERT INTO EMPLOYEE VALUES(%d, '%s', '%s', '%s', '%s', %d, %d, '%s', '%s')" %(slno, name, address, empcode, dob, age, mobile, status, designation)) #execute the insert query with the passed parameters
        self.db.commit()#save changes to the database
        print("INSERTED 1 ROW SUCCESSFULLY")

    def displayAll(self):
        self.cur.execute("SELECT * FROM EMPLOYEE")#query fetches all records in table employee
	results = self.cur.fetchall()#fetches all rows 
	#print the rows
	for row in results:
	    print(row) 
			
    def delete(self,slno):
        q = self.cur.execute("DELETE FROM EMPLOYEE WHERE SL_NO= %d"%(int(slno)))
        #execute the deletion query and save in q
        #if sl_no exists q contains a truthy value
        #else it contains a falsy value which means sl_no does not exist
        if q:
            print("Record is deleted successfully")
            self.db.commit()
        else:
            print("Invalid slno")
            print(str(slno)+" "+"does not exist")

    def cleanUp(self):
        #clean up and close the connections and cursor objects
        self.cur.close()
        self.db.close()

mydbobj = MyDatabase()

while True:
    print("1.Insert\n2.Delete\n3.Display\n4.Exit")
    ch = int(raw_input("Enter Choice: "))

    if ch == 1:
        slno = int(raw_input("Enter SL_NO: "))
        name = raw_input("Enter Name: ")
        address = raw_input("Enter Address: ")
        empcode = raw_input("Enter EmpCode: ")
        dob = raw_input("Enter date of birth in format YYYY-MM-DD: ")
        age = int(raw_input("Enter Age: "))
        mobile = int(raw_input("Enter Mobile Number: "))
        status = raw_input("Enter status: ")
        desg = raw_input("Enter Designation: ")
        mydbobj.insert(slno,name,address,empcode,dob,age,mobile,status,desg)
    

    elif ch==2:
        slno = int(raw_input("Enter SL_NO: "))
        mydbobj.delete(slno)

    elif ch==3:
        mydbobj.displayAll()

    elif ch==4:
        mydbobj.cleanUp()
        exit()

    else:
        print("Invalid Choice")


