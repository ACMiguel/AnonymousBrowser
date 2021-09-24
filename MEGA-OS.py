import time
import os

print("""
███╗░░░███╗███████╗░██████╗░░█████╗░░░░░░░░█████╗░░██████╗
████╗░████║██╔════╝██╔════╝░██╔══██╗░░░░░░██╔══██╗██╔════╝
██╔████╔██║█████╗░░██║░░██╗░███████║█████╗██║░░██║╚█████╗░
██║╚██╔╝██║██╔══╝░░██║░░╚██╗██╔══██║╚════╝██║░░██║░╚═══██╗
██║░╚═╝░██║███████╗╚██████╔╝██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░
""")
print("""
[1] Continue With Setup
[2] Ive Already Done Setup
""")
setup = input("[?]: ")
if setup == '1':
    name = input(str("Please Enter your Username to be Displayed: "))
    pas = input(str("Please enter your Password to Login: "))

    lines =[name]
    with open('user/username.txt', 'w') as f:
        f.writelines(lines)

    lines2 = [pas]
    with open('user/password.txt', 'w') as f:
        f.writelines(lines2)

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Enter the Password to " + l_n + ": "))
    if login == l_p:
        os.startfile("https://github.com/Max-Mega/AnonymousBrowser")
        break
    else:
        print("Wrong Password!")