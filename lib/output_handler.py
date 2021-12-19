from re import match
import os
from lib.logo import print_delimiter

def check_if_file_exists(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
    except:
        print("Error occured while checking if output file already exists")

def write_output_to_a_file(file_path, data):
    if data != None and len(data) > 0:
        delimiter = "=================================================================="
        print("* Writing data to a file %s" % file_path)
        f = open(file_path, "a+")
        f.write(delimiter)
        f.write(data)
        f.write(delimiter)
        f.close()
        print("* Finished writing data to a file %s" % file_path)
