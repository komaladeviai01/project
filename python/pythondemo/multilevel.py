class company():
    def __init__(self):
        print("The company details")

    def companyname(self):
        print(" The company name SBK ")
    def accessnetwork (self):
        print("The company provite network")

class manager(company):
    def __init__(self):
        super().__init__()
        super().companyname()
        super().accessnetwork()
        print("The company details")
        
    def ordertostaff(self):
        print(" Distributed the work properly ")
class visitor(manager):
    pass
              
#a=manager()
#a.ordertostaff()
v=visitor()
