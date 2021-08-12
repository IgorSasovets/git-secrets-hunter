import requests
import os
import subprocess
from pathlib import Path

from lib.logo import print_delimiter
from lib.github_helper import get_user_public_repos
from constant import GITLEAKS_DOWNLOAD_URL,GITLEAKS_BINARY_PATH,GITLEAKS_SCAN_DEPTH

def scan_single_user_repos_using_gitleaks(username):
    print_delimiter()
    print("* Scanning public repositories of %s using gitleaks..." % username)
    clone_urls_list = get_user_public_repos(username)
    for repo_url in clone_urls_list:
        print("* Started scanning of single repository: %s" % repo_url)
        subprocess.call([GITLEAKS_BINARY_PATH, "-r", repo_url, "--depth=%i" % GITLEAKS_SCAN_DEPTH, "-v"])
        print("* Gitleaks scan for %s finished. See above results\n" % repo_url)
    print_delimiter()

def scan_multiple_users_repos_using_gitleaks(usernames_list):
    print_delimiter()
    print("* Started scanning of multiple users repositories using gitleaks...")
    for username in usernames_list:
        scan_single_user_repos_using_gitleaks(username)
    print("* Finished scanning of multiple users repositories")
    print_delimiter()

def download_gitleaks(platform):
    print_delimiter()
    print("* Downloading gitleaks binaries for platform %s..." % platform)
    r = requests.get(GITLEAKS_DOWNLOAD_URL + platform)
    if (r.status_code != 200):
        raise ConnectionError("ERROR: gitleaks-%s download failed" % platform)
    else:
        try:
            print("* Creating folder for binary...")
            os.mkdir(GITLEAKS_BINARY_PATH[:GITLEAKS_BINARY_PATH.rfind("/gitleaks")], 0o755)
        except FileExistsError as err:
            print(err)
            print("* Folder for binary already exists. Skipping this step")
        print("* Writing binary content to a file: %s" % GITLEAKS_BINARY_PATH)
        open(GITLEAKS_BINARY_PATH, "wb").write(r.content)
        print("* Download successfully finished")
        if (platform.find("windows") == -1):
            print("* Making binary executable...")
            os.chmod(GITLEAKS_BINARY_PATH, 0o755)
        print("* gitleaks binary is ready for use")
        print_delimiter()
