import datetime
userdata = {}
while True:
    print('*** Menu ***')
    print('1. Add User')
    print('2. Login')
    print('x. Exit')
    menu = input('Enter a menu: ')
    if menu == 'x':
        print('Thank You')
        break
    elif menu == '1':
        while True:
            username = input("Enter Username: ")
            if username not in userdata:
                break
            else:
                print('Username is duplicate, please try again')
        password = input('Enter Password: ')
        firstname = input('Enter Firstname: ')
        lastname = input('Enter Lastname: ')
        userdata[username] = [password, firstname, lastname]
        print(f"User {username} added successful!")
    elif menu == '2':
        c = 0
        while c < 3:
            inputusername = input("Enter Username: ")
            inputpassword = input("Enter Password: ")
            if inputusername in userdata and inputpassword == userdata[inputusername][0]:
                print(f"Welcome {inputusername[1]} {inputusername[2]}! Login Success Date: ! Login Success Date: {datetime.datetime.now()}")
                break
            else:
                print("Username and Password incorrect!!")
                c += 1
            if c == 3:
                print("You entered too many incorrect usernames and passwords")
                break
    else:
        print("Invalid menu option , Please try again")
