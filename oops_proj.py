class chatbook:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.loggedin=False
        self.menu()
    def menu(self):
        user_input=input("""welcome to chatbook ? to preceed? 
        1.press 1 to signup
        2.press 2 to signin
        3.press 3 to write a post
        4.press 4 to message a friend
        5. press any other key to exit"""
        )
        if user_input=="1":
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()
res =chatbook("harsha",124)