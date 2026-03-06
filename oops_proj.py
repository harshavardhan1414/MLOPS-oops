class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
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
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email=input("enter email->")
        password=input("enter pass here->")
        self.username=email
        self.password=password
        print("signup successfull!!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup first")
        else:
            username=input("enter email->")
            password=input("enter password->")
            if self.username==username and self.password==password:
                print("signed in seccessfull")
                self.loggedin=True
            else:
                print("enter correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("enter ur msg here..")
            print(f"ur post is posted->{txt}")
        else:
            print("signin first")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("enter the msg->")
            frnd=input("whom to send msg->")
            print(f"ur mesg sent{frnd}")
        else:
            print("signin first")
        print("\n")
        self.menu()

# res =chatbook()