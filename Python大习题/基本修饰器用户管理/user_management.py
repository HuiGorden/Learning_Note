# -*- coding: utf-8 -*-
# @Time    : 2018-01-13 9:51 PM
# @Author  : Jin,Hui
# @Email   : gordeninottawa@gmail.com
# @File    : user_management.py
import json
import getpass
import subprocess
import time
import random
import re
Login = False
Coupon_Enable = False
SuperUser_Enable = False
UserName = ""
Coupon_Code = "AE8293EF"
def login():
    username = input("Username:")
    password = getpass.getpass("Password:")
    with open("User_Info", "r") as f:
        userinfo_dict = json.load(f)
        if username in userinfo_dict and password == userinfo_dict[username]["Password"]:
            print("Welcome " + username)
            global Login
            Login = True
            if userinfo_dict[username]["Level"] >= 2:
                global Coupon_Enable
                Coupon_Enable = True
            if userinfo_dict[username]["SuperUser"]:
                global SuperUser_Enable
                SuperUser_Enable = True
            global UserName
            UserName = username
        else:
            print("Login Failed.....")

def register():
    username = input("Username")
    one_password = getpass.getpass("Enter Password:")
    second_password = getpass.getpass("Confirm Password:")
    userinfo_dict = {}
    if one_password == second_password:
        with open("User_Info", "r") as f:
            userinfo_dict = json.load(f)
            if username in userinfo_dict:
                print("Username existed")
                return
            else:
                userinfo_dict[username] = {"Password": one_password, "SuperUser": False, "Level" : 1}
        with open("User_Info", "w") as f:
            json.dump(userinfo_dict, f, indent=2)
            print("Register Successfully, Please Log in")
    else:
        print("Password Unmatched,Register Failed")
        return

def is_login(func):
    def inner():
        if Login and UserName:
            func()
        else:
            print("Please Login First")
    return inner

def is_SuperUser(func):
    def inner():
        if SuperUser_Enable:
            func()
        else:
            if Login and not SuperUser_Enable:
                print("You need to login as SuperUser")
            else:
                print("You need to login first")
    return inner
@is_login
def modify_password():
    one_password = getpass.getpass("Enter Password:")
    second_password = getpass.getpass("Confirm Password:")
    if one_password == second_password:
        global UserName
        f = open("User_Info", "r")
        userinfo_dict = json.load(f)
        f.close()
        userinfo_dict[UserName]["Password"] = one_password
        f = open("User_Info", "w")
        json.dump(userinfo_dict, f, indent=2)
        f.close()
        print("Change Password Succesfully")
    else:
        print("Password Unmatched")
        return

def check_coupon():
    if Coupon_Enable:
        global Coupon_Code
        print("Today Coupon Code is " + Coupon_Code)
    else:
        print("No Permission to view Coupon")
@is_login
def check_account_info():
    info_dict = {}
    f = open("User_Info", "r")
    user_info_dict = json.load(f)
    f.close()
    info_dict = user_info_dict[UserName]
    print("*"*50)
    print("UserName:" + UserName)
    print("SuperUser:" + str(info_dict["SuperUser"]))
    print("Permission Level:" + str(info_dict["Level"]))


@is_SuperUser
def modify_user():
    subprocess.call("clear", shell=True)
    exit_flag = 0
    while not exit_flag:
        print("*"*50)
        print("1.Delete User")
        print("2.Add User")
        print("3.List All User")
        print("4.Search User")
        print("5.Set User Level")
        print("6.Refresh Screen")
        print("7.Back to Upper Level")
        print("*"*50)
        selection = input()
        if selection == "1":
            delete_user()
        elif selection == "2":
            add_user()
        elif selection == "3":
            list_user()
        elif selection == "4":
            search_user()
        elif selection == "5":
            set_user_level()
        elif selection == "6":
            subprocess.call("clear", shell=True)
        elif selection == "7":
            subprocess.call("clear", shell=True)
            return
        else:
            print("Invalid Input")
def delete_user():
    username = input("Enter Target User Name:")
    print("Locating User...")
    time.sleep(3)
    f = open("User_Info", "r")
    user_info_dict = json.load(f)
    f.close()
    if username not in user_info_dict:
        print("User: " + username + " Not Found")
        return
    else:
        del user_info_dict[username]
        print("User " + username + "Delete Completed!")
    f = open("User_Info", "w")
    json.dump(user_info_dict, f, indent=2)
    f.close()
def add_user():
    username = input("Enter User Name:")
    f = open("User_Info", "r")
    user_info_dict = json.load(f)
    f.close()
    if username in user_info_dict:
        print("User: " + username + " in DB already")
        return
    else:
        random_password = password_generator()
        user_info_dict[username] = {}
        user_info_dict[username]["password"] = random_password
        user_info_dict[username]["SuperUser"] = False
        user_info_dict[username]["Level"] = 1
        f = open("User_Info", "w")
        json.dump(user_info_dict, f, indent=2)
        f.close()
        print("User: " + username + "has been added. Default Password Generated:" + random_password + ", Level 1")
def list_user():
    f = open("User_Info", "r")
    user_info_dict = json.load(f)
    f.close()
    for username in user_info_dict.keys():
        print("*"*50)
        print("User: " + username)
        if user_info_dict[username]["SuperUser"]:
            print("SuperUser:Yes")
        else:
            print("SuperUser:No")
        print("Level:" + str(user_info_dict[username]["Level"]))
        print("*"*50)
def search_user():
    print("Which User do you want to find?")
    searching_user = input()
    f = open("User_Info", "r")
    user_info_dict = json.load(f)
    f.close()
    match_flag = 0
    for username in user_info_dict.keys():
        if re.search(r".*"+searching_user+".*", username):
            print("One Match: Username: %s, Level: %s" % (username, str(user_info_dict[username]["Level"])))
            match_flag = 1
    if not match_flag:
        print("No any Match")
def set_user_level():
    print("Which User do you want to set?")
    searching_user = input()
    f = open("User_Info", "r")
    user_info_dict = json.load(f)
    f.close()
    if searching_user not in user_info_dict.keys():
        print("User Not Existed")
        return
    else:
        set_level = input("Which Level do you want to set?")
        try:
            set_level = int(set_level)
        except:
            print("Invalid input")
        user_info_dict[searching_user]["Level"] = set_level
        f = open("User_Info", "w")
        json.dump(user_info_dict, f, indent=2)
        f.close()
        print("Set Sucessfully")
def password_generator():
    each_verification_code = []
    random_length = random.randrange(6,11)
    for each_bit in range(random_length):
        random_type = random.randrange(1, 4)
        if random_type == 1:
            # Number
            each_verification_code.append(str(chr(random.randrange(48, 58))))
        elif random_type == 2:
            # UpperCase Letter
            each_verification_code.append(str(chr(random.randrange(65, 91))))
        else:
            # LowerCase Letter
            each_verification_code.append(str(chr(random.randrange(97, 123))))
    return "".join(each_verification_code)
#main#
exit_flag = 0
subprocess.call("clear", shell=True)
print("*" * 50)
print("Welcome to User Management Program".format(50, "*"))
while not exit_flag:
    if not Login:
        print("1.Login")
    else:
        print("1.Logout")
    if not Login:
        print("2.Register")
    else:
        print("\033[1;31m2.Register\033[0m")
    print("3.Modify Password")
    print("4.Check Today Coupon")
    print("5.Check My Account Info")
    print("6.Manage User DB")
    print("7.Refresh Screen")
    print("8.Exit")
    selection = input()
    if selection == "1" and not Login:
        login()
    elif selection == "1" and Login:
        Login = False
        Coupon_Enable = False
        SuperUser_Enable = False
    elif selection == "2" and not Login:
        register()
    elif selection == "3":
        modify_password()
    elif selection == "4":
        check_coupon()
    elif selection == "5":
        check_account_info()
    elif selection == "6":
        modify_user()
    elif selection == "7":
        subprocess.call("clear", shell=True)
    elif selection == "8":
        exit_flag = 1
    else:
        print("Invalid Input")
    print("*"*50)
subprocess.call("clear", shell=True)


