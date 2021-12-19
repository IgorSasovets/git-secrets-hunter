import inspect
import os
import subprocess

from lib.logo import print_delimiter
from lib.github_helper import get_user_public_repos
from lib.output_handler import write_output_to_a_file
from constant import TRUFFLEHOG_SCAN_DEPTH,TRUFFLEHOG_EXCLUDE_PATTERNS_PATH

def check_if_truffle_hog_installed():
    print_delimiter()
    print("* Checking if truffleHog package is installed...")
    for pip_module in ["pip", "pip3"]:
        try:
            out = subprocess.run([pip_module, "list"], capture_output=True, text=True)
            if len(out.stderr) > 0:
                print("* Error occured when running 'pip list':")
                print(str(out.stderr))
                return False
            else:
                return out.stdout.find("truffleHog") > -1
        except FileNotFoundError as err:
            print("* %s module not found, trying pip3..." % pip_module)

def get_truffle_hog_package_path():
    print_delimiter()
    print("* Getting truffleHog package path...")
    try:
        import truffleHog
        return os.path.dirname(inspect.getfile(truffleHog)) + "/truffleHog.py"
    except:
        print("Error occured while getting truffleHog package path")
        return ""

def scan_single_user_repos_with_truffle_hog(username, output_file):
    print_delimiter()
    truffle_hog_package_path = get_truffle_hog_package_path()
    print("* Scanning public repositories of %s using truffleHog..." % username)
    clone_urls_list = get_user_public_repos(username)
    for repo_url in clone_urls_list:
        args_list = [
            "python3", truffle_hog_package_path,
            "--max_depth", str(TRUFFLEHOG_SCAN_DEPTH), "-x", TRUFFLEHOG_EXCLUDE_PATTERNS_PATH,
            repo_url
        ]
        print("* Started scanning of single repository: %s" % repo_url)
        if output_file != None and output_file != "":
            output = subprocess.run(args_list, capture_output=True, text=True)
            write_output_to_a_file(output_file, output.stdout)
            write_output_to_a_file(output_file, output.stderr)
        else:
            subprocess.call(args_list)
        print("* truffleHog scan for %s finished. See above results\n" % repo_url)
    print_delimiter()

def scan_multiple_users_repos_with_truffle_hog(usernames_list, output_file):
    print_delimiter()
    print("* Started scanning of multiple users repositories using truffleHog...")
    for username in usernames_list:
        scan_single_user_repos_with_truffle_hog(username, output_file)
    print("* Finished scanning of multiple users repositories")
    print_delimiter()