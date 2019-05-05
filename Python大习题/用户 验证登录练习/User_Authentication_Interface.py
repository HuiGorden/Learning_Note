# -*- coding: utf-8 -*-
# @Time    : 2017-12-12 10:38 PM
# @Author  : Jin,Hui
# @Email   : gordeninottawa@gmail.com
# @File    : User_Authentication_Interface.py
import json
import getpass
import os
print("User Authentication Interface Demo\n")
record_dict = {}
if not os.path.exists("record_failed.json"):
    with open('record_failed.json', 'w') as f2:
        f2.write("{}")
        f2.close()
with open('record.json', 'r') as f:
    record_dict = json.load(f)
while 1:
    with open('record_failed.json', 'r') as f2:
        failed_record_dict = json.load(f2)
    username = input("Please enter your username:")
    password = getpass.getpass("Please enter your password:")
    if username in failed_record_dict.keys() and failed_record_dict[username] >= 3:
        print(username+" Login Failed")
        break
    elif username in record_dict.keys() and record_dict[username] == password:
        print("Welcome "+username)
        break
    else:
        print(username+" Login Failed")
        if username in failed_record_dict.keys():
            failed_record_dict[username] += 1
            if failed_record_dict[username] >= 3:
                print(username + "has been locked!")
                with open('record_failed.json', 'w') as f2:
                    json.dump(failed_record_dict, f2, indent=2)
                break
        else:
            failed_record_dict[username] = 1
        with open('record_failed.json', 'w') as f2:
            json.dump(failed_record_dict, f2, indent=2)
