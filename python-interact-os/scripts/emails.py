#!/usr/bin/env python3

import sys
import csv

def populate_dictionary(filename):
    """ Populate a dict with name/email pairs for easy lookup. """
    email_dict = {}
    with open(filename) as csv_file:
        lines = csv.reader(csv_file, delimiter=',')
        for row in lines:
            full_name = row[0].lower()
            email = row[1]
            email_dict[full_name] = email
    return email_dict

def find_email(argv):
    """ Return an email address based on the username given. """
    try:
        full_name = argv[1] + " " + argv[2]
        email_dict = populate_dictionary("./python-interact-os/data/user_emails.csv")
        if email_dict.get(full_name.lower()):
            return email_dict.get(full_name.lower())
        return "No email address found"
    except IndexError:
        return "Missing parameters"

def main():
    print(find_email(sys.argv))

if __name__ == "__main__":
    main()
