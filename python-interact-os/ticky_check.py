#!/usr/bin/env python3

import re
import operator
import csv


with open("./syslog.log", 'r') as syslog:
    log = syslog.read()
    error_patterm = r"ERROR\s([\w*\s\']*)"
    error_list = re.findall(error_patterm, log)
    error_dict = {}
    for error in error_list:
        if error not in error_dict:
            error_dict[error] = error_list.count(error)
    sorted_tuples = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_error_dict_data = [{"Error": k.strip(), "Count": v} for k, v in sorted_tuples]
    csv_columns = ["Error", "Count"]
    csv_file = "error_message.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in sorted_error_dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error in process error_message.csv file")
    

    error_user_patterm = r"ERROR.*\((\w+\.*\w+)\)"
    error_list_user = re.findall(error_user_patterm, log)
    info_user_patterm = r"INFO.*\((\w+\.*\w+)\)"
    info_list_user = re.findall(info_user_patterm, log)
    user_error_dict = {}
    user_info_dict = {}
    for user in error_list_user:
        if user not in user_error_dict:
            user_error_dict[user] = error_list_user.count(user)
    for user in info_list_user:
        if user not in user_info_dict:
            user_info_dict[user] = info_list_user.count(user)
    user_info_error_tuple = []
    for user in user_error_dict:
        if user in user_info_dict:
            tuple = (user, user_info_dict[user], user_error_dict[user])
        else:
            tuple = (user, 0, user_error_dict[user])
        user_info_error_tuple.append(tuple)
    user_info_error_tuple.sort()
    user_info_error_dict_data = [{"Username": user, "INFO": info, "ERROR": error} for user, info, error in user_info_error_tuple]
    csv_columns = ["Username", "INFO", "ERROR"]
    csv_file = "user_statistics.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in user_info_error_dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error in process user_statistics.csv file")

    
