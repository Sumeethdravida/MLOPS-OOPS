class EightMate:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to EightMate! How would you like to proceed?
                           1.Press 1 to signup
                           2.Press 2 to sign in
                           3.Press 3 to write a post
                           4.Press 4 to message a friend
                           5.Press any other key to exit
                           : """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        
    def signup (self):
        email = input("Enter you email here: ")
        password = input("Enter your password here: ")
        self.username = email
        self.password = password
        print("You have signed up successfully!")
        print("\n")
        self.menu()
        


obj = EightMate()
