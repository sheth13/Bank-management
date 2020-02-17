def Display():
    print('1.Login')
    print('2.Registration') 
    print('3.exit')

    proceed = input("proceed : ")
    if proceed==1:
        pass
    elif proceed==2:
        Registration()
    elif proceed==3:
        pass

def Registration():
    print("\n        Details\n")
    name = str(input("Name : "))
    email = input("Email: ")
    username = input("Username : ")
    password = input("Password : ")
    re_enter = input("Re-enter Passworld : ")
    if password==re_enter:
        print("\nRegistration completed successfully")
    else:
        print("\nPassword do not macth")

def Exit():
    e = input("press any key to return : ")
    if e==e:
        Display()
    else:
        pass
