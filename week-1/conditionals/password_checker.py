''' a simple login check comparing an entered
password to a stored one;'''
username="pavansai91@gmail.com"
password = "pavan123@"
enter_username = input("enter username : ")
enter_password = input("enter password : ")

if enter_username == username and enter_password == password:
    print("login succesful")
else:
    print("incorrect details")
