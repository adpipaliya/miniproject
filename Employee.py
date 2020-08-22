
from PermanentEmployee import Per_Emp
from validation import Validation
from connect import myconnect
class Employee:

      _empname=""
      _emptype=""
      _empemail=""
      _empsalary=""

      def __init__(self):
            self._empname = input("Enter The Name: ")
            self._empemail=input("Enter The Email: ")
            e_val = Validation()
            if(e_val.validateemail(self._empemail) == False):
                  exit(0)
            self._empmob=input("Enter The Mobileno: ")
            if(e_val.validatemobile(self._empmob) == False):
                  exit(0)
            self._emptype = input("Enter The  Type: ")
            self._empexp = int(input("Enter Your Experience: "))
            self._empsalary = self.getsalary()
            
      def getsalary(self):
            if self._emptype=="P" or self._emptype=="p":
                  Opemp = Per_Emp()
                  return Opemp.calculatesalary(self._empexp)
            else:
                  print("You Entered Invalid Input. Please enter only 'p' or 'P'")
                  
      
      @staticmethod
      def addnote():
            note = input("Enter a note : ")
            notef=open("note.txt","a+")
            notef.write("\n")
            notef.write(note)
            notef.close()
                  
print("1. Add Employee Detail")
print("2. Display Employee Detail")
print("3. Add Notes")
choice = int(input("Enter The Choice:"))
if choice == 1:
      a = Employee()
      obj = myconnect()
      obj.savetodb(a._empname,a._empemail,a._empmob,a._emptype,a._empexp,a._empsalary)
elif choice==2:
      obj = myconnect()
      obj.display()
elif choice==3:
      Employee.addnote()
else:
      print("You Enter Invalid Choice")