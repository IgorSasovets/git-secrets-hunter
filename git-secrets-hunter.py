import subprocess
import argparse
from re import match

# Import custom lib modules
from lib.logo import *
from lib.github_helper import *
from lib.gitleaks_helper import *
from lib.file_reader import *
import constant

def validate_arguments(file_path, platform, username, mode):
    match_res = match("[a-zA-Z\/.]+", file_path)
    if (match_res != None and match_res.span()[1] != len(file_path)):
        raise ValueError("ERROR: File path is incorrect")
    match_res = match("\B@([a-z0-9](?:-?[a-z0-9]){0,38})", username)
    if (match_res != None and match_res.span()[1] != len(username)):
        raise ValueError("ERROR: Username is incorrect")
    constant.GITLEAKS_PLATFORMS_LIST.index(platform)
    constant.PROGRAM_MODES_LIST.index(mode)
    
def print_error_message(err = ""):
    print("Invalid params provided. Please run again with -h option to get available arguments")
    print(err)

def run_program(file_path, username, mode):
    if (username != "" and mode == constant.PROGRAM_MODES_LIST[0]):
        scan_single_user_repos_using_gitleaks(username)
    if (file_path != "" and mode == constant.PROGRAM_MODES_LIST[1]):
        usernames_list = read_github_usernames_from_file(file_path)
        scan_multiple_users_repos_using_gitleaks(usernames_list)

def main():
    try:
        print_logo()
        parser = argparse.ArgumentParser(description="Git secrets hunter options:")
        parser.add_argument("-f", "--file", 
            help="path of a file that contains list of GitHub usernames", type=str, default="")
        parser.add_argument("-u", "--username", 
            help="GitHub username of a target", type=str, default="")
        parser.add_argument("-m", "--mode", 
            help="run mode. Available modes: {}".format(constant.PROGRAM_MODES_LIST), type=str, default="scan_single_user")
        parser.add_argument("-p", "--platform",
            help="OS platform (for gitleaks), available platforms: {}".format(constant.GITLEAKS_PLATFORMS_LIST),
            type=str, default="linux-amd64")
        args = parser.parse_args()
        file_path, platform, username, mode = (args.file.strip(), args.platform, args.username.strip(), args.mode)
        if (file_path == "" and username == ""):
            raise ValueError("ERROR: You should always specify file_path or username")
        validate_arguments(file_path, platform, username, mode)
        download_gitleaks(platform)
        run_program(file_path, username, mode)
    except KeyboardInterrupt:
        print("\n[*] User requested an interrupt")
        print("[*] Application exiting...")
        sys.exit()
    except ValueError as err:
        print_error_message(err)
    except AttributeError as err:
        print_error_message(err)
    except ConnectionError as err:
        print(err)

if __name__ == "__main__":
    main()