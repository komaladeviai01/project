class parent():
    def __init__(self):
        print("App access to your information")

    def AccessChrome(self):
        print("login ")
    def Name(self):
        print("Enter the name")
    def Email(self):
        print("Enter the email" )
    def OTP(self):
        print("would you enter the OTP")
class child(parent):
    def __init__(self):
        super().__init__()
        super().AccessChrome()
        super().Name()
        super().Email()
        super().OTP()
    

        
        
    

