class chatbook:
    def __init__(self):
        self.__name="DU"
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name=value
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
#getter and setter method
# def add(self,*args) method overloading

class animal:
    #defining constructer
    def __init__(self,name="Unknown"):
        self.name=name
        print("animal constructer called")
    #instance method
    def speak(self):
        print(self.name,"makes a sound")
    #method overloading sim using *args
    def info(self,*args):
        if len(args)==1:
            print("animal age:",args[0])
        elif len(args)==2:
            print("animal age:",args[0],"weight:",args[1])
        else:
            print("no add info")
    #Static method
    def kingdom():
        print("all ")
    def class_info(cls):
        print("this is animal class")
class dog(animal):
    #constructor overriding
    def __init__(self, name,breed="Unknown"):
        super().__init__(name)
        self.breed=breed
        print("dog con called")
    #method overriding
    def speak(self):
        print(self.name,"barks")
d1=dog("rock","lab")
print("metho overlrriding")
d1.speak()
print("met overloading")
d1.info(5)
d1.info(5,20)