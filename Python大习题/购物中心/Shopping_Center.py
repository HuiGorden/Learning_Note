# -*- coding: utf-8 -*-
# @Time    : 2017-12-30 8:20 PM
# @Author  : Jin,Hui
# @Email   : gordeninottawa@gmail.com
# @File    : Shopping_Center.py
import subprocess
import json
import time
from datetime import datetime
def show_item_menu(recorder):
    menu_dict = {}
    with open('Shopping_menu.json', 'r') as f:
        menu_dict = json.load(f)
    tmp_menu_dict = menu_dict
    # Show selection path
    for i in travse_list:
        print(i + "-->", end='')
    print("")
    if not recorder:
        keys = list(menu_dict.keys())
        transfer_dict.clear()
        for i in list(range(0, len(keys))):
            print(str(i+1) + ":"+keys[i])
            transfer_dict[str(i + 1)] = keys[i]
    else:
        # Step into menu, following user selection
        for i in travse_list:
            tmp_menu_dict = tmp_menu_dict[i]
        #####Below has deeper dict
        if 'dict' in str(type(tmp_menu_dict)) and 'price' in tmp_menu_dict:
            print(recorder[-1]+"  Left:"+str(tmp_menu_dict['left'])+"  Price:"+str(tmp_menu_dict['price'])+" Do you want to buy?")
            print("1.Buy")
            print("2.Back")
            selection=input()
            if selection == "2":
                print("------------------------")
                pass
            elif selection == "1":
                if tmp_menu_dict['left'] == 0:
                    print("Not enough storage,Not able to process")
                else:
                    with open('Shopping_Member.json', 'r+') as f2:
                        member_info = json.load(f2)
                        balance = member_info[member_id]['balance']
                        with open('Shopping_menu.json', 'r+') as f:
                            updated_menu_dict = json.load(f)
                            menu_dict = updated_menu_dict
                            for i in travse_list:
                                updated_menu_dict = updated_menu_dict[i]
                            if updated_menu_dict['price'] > balance:
                                print("Sorry, you don't have enough money for this,Please recharge")
                            else:
                                updated_menu_dict['left'] = updated_menu_dict['left'] - 1
                                member_info[member_id]['balance'] = member_info[member_id]['balance'] - updated_menu_dict['price']
                                member_info[member_id]['history'].append("Purchased "+ recorder[-1] +" on "+str(datetime.now().strftime("%Y/%m/%d %X")))
                                with open('Shopping_menu.json', 'w+') as f:
                                    json.dump(menu_dict,f, indent=2)
                                with open('Shopping_Member.json','w+') as f:
                                    json.dump(member_info,f, indent=2)
                                print("Purchased successfully")
            else:
                print("Invalid Selection")
            ####If touch lowest level regenerate tmp_menu_dict#
            travse_list.pop()
            tmp_menu_dict = menu_dict
            for i in travse_list:
                tmp_menu_dict = tmp_menu_dict[i]
            keys = list(tmp_menu_dict.keys())
            # construct number to option
            transfer_dict.clear()
            for i in list(range(0, len(keys))):
                print(str(i + 1) + ":" + keys[i])
                transfer_dict[str(i + 1)] = keys[i]
            ####################################################
        elif 'dict' in str(type(tmp_menu_dict)):
            keys = list(tmp_menu_dict.keys())
            # construct number to option
            transfer_dict.clear()
            for i in list(range(0, len(keys))):
                print(str(i + 1) + ":" + keys[i])
                transfer_dict[str(i+1)] = keys[i]
        else:
            print(tmp_menu_dict)
            transfer_dict.clear()
    print("Type 'b' to upper level")


def login_or_register():
    exit_flag = 0
    while not exit_flag:
        print("1. Sign in as existing member")
        print("2. Sign up as new member")
        print("3. Exit")
        selection = input("")
        if selection == "1":
            member_id = input("Member Name:")
            member_password = input("Member Password:")
            with open('Shopping_Member.json', 'r') as f:
                member_info = json.load(f)
                if member_id in member_info.keys() and member_info[member_id]['password'] == member_password:
                    print(("Login Succesfully, Your balance is " + str(member_info[member_id]['balance'])).center(50, "*"))
                    return member_id
                else:
                    if member_id not in member_info.keys():
                        print("Member is not existed")
                    else:
                        print("Login Failed")
        elif selection == "2":
            member_id = input("Member Name:")
            member_password_first = input("Member Password:")
            member_password_second = input("Retype Member Password:")
            if member_password_first != member_password_second:
                print("Password Unmatched")
                continue
            else:
                with open('Shopping_Member.json', 'r') as f:
                    member_info = json.load(f)
                    if member_id in member_info.keys():
                        print("Member ID is existed")
                    else:
                        member_info[member_id] = {
                            'member_password': member_password_first,
                            'balance': 0,
                            'history': [],
                        }
                with open('Shopping_Member.json', 'w+') as f:
                    json.dump(member_info, f, indent=2)
                print("Sign up sucessfully ,Please Login again")
        elif selection == "3":
            print("See you soon".center(100,"*"))
            exit(1)
        else:
            print("Options not available, please type again")


# #########Main#############
# Clean screen content
subprocess.call("clear",shell=True)
# Used to transfer number to key
transfer_dict = {}
print("Welcome to SuperMarker".center(50, "*"))
# MemberID
member_id = login_or_register()
while 1:
    print("1.Enter SuperMarket")
    print("2.Show my Balance")
    print("3.Recharge membership card")
    print("4.Show purchased history")
    print("5.Refresh Console")
    print("6.exit")
    selection = input()
    if selection == "1":
        # Used to record user selection
        travse_list = []
        show_item_menu(travse_list)
        while 1:
            print("------------------------")
            select = input("Enter your input:")
            if select == "b" and len(travse_list) >= 1:
                travse_list.pop()
                show_item_menu(travse_list)
            elif select == "b" and len(travse_list) == 0:
                break
            elif str(select) in transfer_dict.keys():
                travse_list.append(transfer_dict[str(select)])
                show_item_menu(travse_list)
            else:
                print("Umm, Option not available")
            print(transfer_dict)
    elif selection == "2":
        with open('Shopping_Member.json', 'r') as f:
            member_info = json.load(f)
            print("Your current balance is  "+str(member_info[member_id]['balance']))
    elif selection == "3":
        money_amount = input("How much do you want to transfer?")
        print("Processing.....")
        with open('Shopping_Member.json', 'r') as f:
            member_info = json.load(f)
            member_info[member_id]['balance'] = str(float(member_info[member_id]['balance']) + float(money_amount))
            with open('Shopping_Member.json', 'w+') as f2:
                json.dump(member_info, f2, indent=2)
            time.sleep(2)
            print("Recharge Completed")
    elif selection == "4":
        with open('Shopping_Member.json', 'r') as f:
            member_info = json.load(f)
        if member_info[member_id]['history']:
            for i in member_info[member_id]['history']:
                print("-".center(50, "-"))
                print(i)
            print("-".center(50, "-"))
        else:
            print("-".center(50, "-"))
            print("No purchased record found!!")
            print("-".center(50, "-"))
    elif selection == "5":
        subprocess.call("clear",shell=True)
    elif selection == "6":
        print("See you soon".center(100, "*"))
        exit(1)
    else:
        print("Not Valid selection")
