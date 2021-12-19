import argparse
from re import match

# Import custom lib modules
from lib.logo import *
from lib.github_helper import *
from lib.gitleaks_helper import *
from lib.file_reader import *
from lib.truffle_hog_helper import *
from lib.output_handler import *
import constant

def validate_arguments(file_path, platform, username, scanner, output_file):
    if file_path != "":
        match_res = match("[a-zA-Z\/.]+", file_path)
        if match_res == None or (match_res != None and match_res.span()[1] != len(file_path)):
            raise ValueError("ERROR: Input file path is incorrect")
    if username != "":
        match_res = match("([A-Za-z0-9](?:-?[A-Za-z0-9]){0,38})", username)
        if match_res == None or (match_res != None and match_res.span()[1] != len(username)):
            raise ValueError("ERROR: Username is incorrect")
    if scanner == constant.SCANNERS_LIST[0] or scanner == constant.SCANNERS_LIST[1]:
        constant.GITLEAKS_PLATFORMS_LIST.index(platform)
    constant.SCANNERS_LIST.index(scanner)
    match_res = match("[a-z\/.]+.(log|txt)", output_file)
    if match_res == None or (match_res != None and match_res.span()[1] != len(output_file)):
        raise ValueError("ERROR: Output file path is incorrect. Acceptable formats: .log, .txt")
    
def print_error_message(err = ""):
    print("Invalid params provided. Please run again with -h option to get available arguments")
    print(err)   

def run_program(file_path, username, scanner, output_file):
    check_if_file_exists(output_file)
    if username != "":
        if (scanner == constant.SCANNERS_LIST[0] or scanner == constant.SCANNERS_LIST[1]):
            scan_single_user_repos_using_gitleaks(username, output_file)
        if (scanner == constant.SCANNERS_LIST[0] or scanner == constant.SCANNERS_LIST[2]):
            scan_single_user_repos_with_truffle_hog(username, output_file)
    if file_path != "":
        usernames_list = read_github_usernames_from_file(file_path)
        if scanner == constant.SCANNERS_LIST[0] or scanner == constant.SCANNERS_LIST[1]:
            scan_multiple_users_repos_using_gitleaks(usernames_list, output_file)
        if scanner == constant.SCANNERS_LIST[0] or scanner == constant.SCANNERS_LIST[2]:
            scan_multiple_users_repos_with_truffle_hog(usernames_list, output_file)

def main():
    try:
        print_logo()
        parser = argparse.ArgumentParser(description="Git secrets hunter options:")
        parser.add_argument("-f", "--file", 
            help="path to a file that contains list of GitHub usernames", type=str, default="")
        parser.add_argument("-u", "--username", 
            help="GitHub username of a target", type=str, default="")
        parser.add_argument("-s", "--scanner", 
            help="scanner to use. Available options: {}".format(constant.SCANNERS_LIST), type=str, default=constant.SCANNERS_LIST[0])
        parser.add_argument("-p", "--platform",
            help="OS platform (for gitleaks), available platforms: {}".format(constant.GITLEAKS_PLATFORMS_LIST),
            type=str, default="linux-amd64")
        parser.add_argument("-o", "--output-filename", 
            help="name of file where to save run results(.log, .txt). If file exists, it will be deleted.", type=str, default="")
        args = parser.parse_args()
        file_path, platform, username, scanner, output_file = (args.file.strip(), args.platform, args.username.strip(),
            args.scanner.strip(), args.output_filename.strip())
        if file_path == "" and username == "":
            raise ValueError("ERROR: You should always specify file_path or username")
        validate_arguments(file_path, platform, username, scanner, output_file)
        run_program(file_path, username, scanner, output_file)
        if output_file != None and output_file != "":
            print("[*] Detected by the scanners information was saved to a %s" % output_file)
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