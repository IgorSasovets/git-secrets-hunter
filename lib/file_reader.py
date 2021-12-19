from re import match
from lib.logo import print_delimiter

def read_github_usernames_from_file(file_path):
    print_delimiter()
    usernames_list = []
    print("* Retrieving list of GitHub usernames from %s" % file_path)
    f = open(file_path, "r")
    for line in f:
        line = line.strip()
        match_res = match("([A-Za-z0-9](?:-?[A-Za-z0-9]){0,38})", line)
        if match_res == None or (match_res != None and match_res.span()[1] != len(line)):
            print("* Username %s is incorrect. Skipping it..." % line)
        else:
            print("* Username %s is valid. Adding it to the list..." % line)
            usernames_list.append(line)
    f.close()
    print("* Extracted list of usernames from %s" % file_path)
    print_delimiter()
    return usernames_list
