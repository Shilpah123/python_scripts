
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 09:05:00 2023

@author: sh001
"""
# This script will upload the zip file to usnav server (based on the path defined in files.put line) and unzips it.
# The time taken for upload is also printed once the upload is done.
#Keep the paths and zip file names constant so that you do not have to update it every time.

#You must update the path and zip file names - change lines 39, 43, 49, 56, 65.

import paramiko
import time
import sys
import random



# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = ""
username = ""
password = ""


ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,username=username,password=password)

print('connection established successfully')

# create an SFTP client object
ftp = ssh_client.open_sftp()

#remove directory

stdin, stdout, stderr = ssh_client.exec_command('rm -rf * //remote server path')
print('Removed directory')

#create directory
stdin, stdout, stderr = ssh_client.exec_command('mkdir //remote server path')
print('Created directory')

print('Zip file upload in progress')
start = time.time()
# Upload a file to the remote server
files = ftp.put("local directory path//abc.zip","//remote server path//abc.zip")
elapsed = time.time() - start
print("Complete!")


#Unzip

stdin, stdout, stderr = ssh_client.exec_command('cd //remote server path//; unzip -o abc.zip')
print(stdout.read().decode())
    
print('Unzipped the files')

print('Time taken to upload zip:')
print (time.time() - start)

stdin, stdout, stderr = ssh_client.exec_command('cd //remote server path//; chmod 777 *')
#time.sleep(5)


# close the connection
ftp.close()

ssh_client.close()