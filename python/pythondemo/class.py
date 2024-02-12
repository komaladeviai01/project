class grandparents:
    def __init__(self,grandfather,grandmother,familyname):
        self.grandfather=grandfather
        self.grandmother=grandmother
        self.familyname=familyname
    
    def welcome(self):
        print("Hi welcome to", self.familyname ,"family!wishes for",self.grandmother,"and",self.grandfather)

#x=grandparents("bala","kani","BK")
#x.welcome()

class parents(grandparents):
    def __init__(self,fathername,mothername,grandfather,grandmother,familyname):
        self.fathername=fathername
        self.mothername=mothername
        super().__init__(grandfather,grandmother,familyname)

    def thanks(self):
        print("This is ",self.familyname,"family function",self.grandfather,"and ",self.grandmother,"60th wedding Anniversary so",self.fathername,"and",self.mothername,"calibrate with our family friends and relatives")
x =grandparents("bala","kani","BK")
x.welcome()        
y =parents("ravi","mari","bala","kani","Bk")
y.thanks()    

