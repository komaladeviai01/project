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
        print ("The control of company")
class manager(company):
    def __init__(self):
        super(). companyname()
        super().accessnetwork()
        super().Id()
        super().password()
    def ordertostaff(self):
        print(" Distributed the work properly ")
    def communicate(self):
        print("The staff proplem or company work  ")
              
class customer(company):
    def __init__(self):
        super().__init__()
        super().companyname()
    def feelpack(self):
        print("The how it is work ")
    def regiment(self):
        print("Thery are regiment this company")


x=company()
y=manager()
z=customer()

        
        
    

