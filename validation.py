import re

class Validation:
    def validateemail(self,email):
        pattern = re.compile(r"[.A-Za-z0-9-]+@[A-Za-z.-]+[.A-Za-z0-9.-]")
        if(pattern.match(email)):
            return email
        else:
            print("This Is Invalid Email Type!!!!!!")
            return False
    def validatemobile(self,mob):
        pattern = re.compile(r"\d{10}")
        if(pattern.match(mob)):
            return mob
        else:
            print("You Entered The Invalid Mobile Number Type!!!!!!")
            return False
