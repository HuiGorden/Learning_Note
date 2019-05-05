# -*- coding: utf-8 -*-
# @Time    : 2017-12-18 12:53 AM
# @Author  : Jin,Hui
# @Email   : gordeninottawa@gmail.com
# @File    : Mutiple_Level_Menu.py
import subprocess
menu_dict = {
    "Car": {
        "Japan": {
            "Honda": {
                "Civic": "2 Left",
                "Accord": "3 Left",
            },
            "Toyota": {
                "Camero": "Sold Out",
            }
        },
        "German": {
            "BMW": {
                "Sedan": {
                    "320xDrive": "Sold out",
                    "428xDrive": "2 Left",
                },
                "SUV": {
                    "X1": "Sold Out",
                    "X6": "On sale"
                }
            },
            "Audi": {
                "Q3": "On sale",
                "Q5": "Delivering"
            }
        }
    },
    "Food": {
        "Fruit": {
            "Apple": "2 dollars/pound",
            "Pineapple": "3 dollars/pound"
        },
        "Meat": {
            "Beef": "Sold Out",
            "Chicken": "10 dollars/pound"
        }
    }
}


def show_menu(recorder):
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
        if 'dict' in str(type(tmp_menu_dict)):
            keys = list(tmp_menu_dict.keys())
            # construct number to option
            transfer_dict.clear()
            for i in list(range(0, len(keys))):
                print(str(i + 1) + ":" + keys[i])
                transfer_dict[str(i+1)] = keys[i]
        else:
            print(tmp_menu_dict)
            print("Type 'b' to upper level")
            transfer_dict.clear()


# #########Main#############
# Used to record user selection
travse_list = []
# Used to transfer number to key
transfer_dict = {}
print("Welcome to SuperMarker,Check our menu,type 'b' to upper level menu, type 'q' to exit")
show_menu(travse_list)
while 1:
    print("------------------------")
    select = input("Enter your input:")
    if select == "q":
        print("See you!")
        break
    elif select == "b" and len(travse_list) >= 1:
        travse_list.pop()
        show_menu(travse_list)
    elif str(select) in transfer_dict.keys():
        travse_list.append(transfer_dict[str(select)])
        show_menu(travse_list)
    else:
        print("Umm, Option not available")
###########################



