class company():
    def __init__(self):
        print("The company details")

    def companyname(self):
        print(" The company name SBK ")
    def accessnetwork (self):
        print("The company provite network")
    def Id (self):
        print("The id corde access" )
    def password(self):
        print("Allow to changed password of system")
    def shareholder(self):
        print ("The control of company....")
class manager():
    def __init__(self):
        print("Welcome to SBK company")
    def ordertostaff(self):
        print(" Distributed the work properly ")
    def communicate(self):
        print("The staff proplem or company work  ")
              
class customer(company,manager):
    def __init__(self):
        super().__init__()
        super().companyname()
        super().accessnetwork()
        super().Id()
        super().password()
        super().shareholder()
        super().__init__()
        super().ordertostaff()
        super().communicate()


   

c=customer()


        
        
    

