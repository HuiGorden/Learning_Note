# -*- coding: utf-8 -*-
# @Time    : 2018-01-07 9:29 PM
# @Author  : Jin,Hui
# @Email   : gordeninottawa@gmail.com
# @File    : HadoopProxyTool.py
import json
import subprocess
import re
from datetime import datetime


def check_existing_record():
    backend = input("Please enter your backend:")
    try:
        records = []
        output_flag = 0
        f = open("Configuration", "r")
        for line in f:
            if output_flag == 0 and re.search(r"^backend"+" "+backend+"\n", line):
                output_flag = 1
            elif output_flag == 1 and re.search(r"^\s+server", line):
                records.append(line.strip())
            elif output_flag == 1 and not re.search(r"^\s+server", line):
                output_flag = 0
            else:
                pass
        f.close()
        if len(records):
            print("For "+backend+":")
            print("\n".join(records))
        else:
            print("No record found!")
    except:
        print("Error Detected,Contact Admin")
def check_json_legal(json_string):
    try:
        return json.loads(json_string)
    except:
        return "Wrong Format"
def check_if_record_exist(backend,record_string):
    with open("Configuration","r") as f:
        match_backend = 0
        for line in f:
            if re.search(r"^backend", line):
                if re.search(r"^backend"+" "+backend, line):
                    match_backend = 1
                else:
                    match_backend = 0
            elif re.search(record_string, line) and match_backend:
                return 1
        return 0
def show_all_record():
    backend_detected = 0
    all_record_json = {}
    f = open("Configuration", "r")
    for line in f:
        if re.search(r"^backend ([\w\.]+)$",line):
            match = re.search(r"^backend ([\w\.]+)$",line)
            backend_detected = match.group(1)
            all_record_json[backend_detected] = []
        elif backend_detected and re.search(r"^\s+([\w\.\s]+)$", line):
            record = re.search(r"^\s+([\w\.\s]+)$", line)
            all_record_json[backend_detected].append(record.group(1).strip())
        else:
            backend_detected = 0
    return all_record_json
def add_proxy_record():
    print("Please Enter your added record")
    print("(foramt:{\"backend\": \"test.oldboy.org\",\"record\":{\"server\": \"100.1.7.9\",\"weight\": 20,\"maxconn\": 30}})")
    added_string = input()
    added_string = added_string.strip()
    added_json = check_json_legal(added_string)
    ###Judge if input is legal###
    if 'str' in str(type(added_json)):
        print("Wrong Format, Unable to process")
        return
    #############################
    written_flag = 0
    backend = added_json['backend']
    record_string = "        " + "server " + added_json['record']['server'] + " " + added_json['record']['server'] + " weight " + str(added_json['record']['weight']) + " maxconn " + str(added_json['record']['maxconn'])
    ####Judge if record existed##
    existed_info = show_all_record()
    if backend in existed_info and record_string.strip() in existed_info[backend]:
        print("Record existed, No need to add")
        return
    #############################
    with open("Configuration", "r") as f1, open("Configuration_New", "w") as f2:
        for line in f1:
            if re.search(r"^backend"+" "+backend, line):
                written_flag = 1
                f2.write(line)
                f2.write(record_string+"\n")
            else:
                f2.write(line)
    if not written_flag:
        f = open("Configuration_New", "a")
        f.write("\n")
        f.write("backend "+backend+"\n")
        f.write(record_string)
        f.close()
    subprocess.call("cp Configuration " + "Configuration_"+str(datetime.now()).replace(" ", "_").replace(":", "_"), shell=True)
    subprocess.call("rm -f Configuration", shell=True)
    subprocess.call("mv Configuration_New Configuration", shell=True)
    print("Added Sucessfully!")
def delete_record():
    '''
     first, we take a look at existed_info to see if record existed,
     secondly, if there is no record, we delete its domain at the same time
     therefore, when we loop to domain line, suspend to write into new configuration file, delete that line in array
     when encounter not server line, we flush record, and then keep writing left lines from original configuration file
    '''
    print("Please Enter your Deleted record")
    print("(foramt:{\"backend\": \"test.oldboy.org\",\"record\":{\"server\": \"100.1.7.9\",\"weight\": 20,\"maxconn\": 30}})")
    writable_flag = 1
    deleted_string = input()
    deleted_string = deleted_string.strip()
    Deleted_json = check_json_legal(deleted_string)
    ###check if input legal######
    if 'str' in str(type(Deleted_json)):
        print("Wrong Format")
        return
    #############################
    backend = Deleted_json['backend']
    record_string = "        " + "server " + Deleted_json['record']['server'] + " " + Deleted_json['record'][ 'server'] + " weight " + str(Deleted_json['record']['weight']) + " maxconn " + str(Deleted_json['record']['maxconn'])
    ####Judge if record existed##
    existed_info = show_all_record()
    if backend not in existed_info or record_string.strip() not in existed_info[backend]:
        print("Record not existed, Unable to Delete")
        return
    #############################
    existed_info[backend].remove(record_string.strip())
    with open("Configuration", "r") as f1, open("Configuration_New", "w") as f2:
        for line in f1:
            if re.search(r"^backend"+" "+backend, line):
                writable_flag = 0
                if len(existed_info[backend]) > 0:
                    f2.write("backend " + backend + "\n")
                    for each_record in existed_info[backend]:
                        f2.write("        " + each_record + "\n")
                for line2 in f1:
                    if re.search(r"^\s+server",line2):
                        pass
                    else:
                        written_flag = 1
                        break
            elif writable_flag:
                f2.write(line)
    subprocess.call("cp Configuration " + "Configuration_"+str(datetime.now()).replace(" ", "_").replace(":", "_"), shell=True)
    subprocess.call("rm -f Configuration", shell=True)
    subprocess.call("mv Configuration_New Configuration", shell=True)
    print("Deleted Sucessfully!")
exit_flag = 0
subprocess.call("clear", shell=True)
print("Python Tool to Modify Hadoop Configuration".center(50,"-"))
while not exit_flag:
    print("*"*50)
    print("1.Show Domain and Corresponding Record")
    print("2.Check existing record")
    print("3.Add Proxy record")
    print("4.Delete Proxy record")
    print("5.Refresh Screen")
    print("6.Exit")
    print("*" * 50)
    selection = input("Please select options:")
    if selection == "1":
        print(json.dumps(show_all_record(), indent=2))
    elif selection == "2":
        check_existing_record()
    elif selection == "3":
        add_proxy_record()
    elif selection == "4":
        delete_record()
    elif selection == "5":
        subprocess.call("clear", shell=True)
    elif selection == "6":
        exit_flag = 1
    else:
        print("Illegal Input...")


