import sqlite3
class myconnect:
      
      def __init__(self):
            
            self.connection = sqlite3.connect("emp.db")
            
            try:
                  self.connection.execute('''create table if not exists employee(
                        emp_name text,
                        email text,
                        mobile text,
                        emp_type char,
                        emp_salary integer,
                        emp_exp integer
                  )''')
                  print("Database Is Created Successfully!")
            except:
                  pass
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            
            self.connection.execute("insert into employee values (?,?,?,?,?,?)",(ename,eemail,emob,etype,eexp,esalary))
            self.connection.commit()

      def display(self):
            
            e_name = input("Enter the employee: ")
            show_data = self.connection.execute("select * from employee where emp_name=:emp_name",{"emp_name":e_name})
            

            for i in show_data:
                  print("Name :",i[0])
                  print("Email :",i[1])
                  print("Mobile No. :",i[2])
                  print("Job Type :",i[3])
                  print("Experience :",i[4])
                  print("Salary :",i[5])