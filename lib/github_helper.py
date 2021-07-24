import requests
import sys
from lib.logo import *

def get_clone_urls(repos_list):
    urls = []
    for repo in repos_list:
        # repos_list has type dict
        urls.append(repo['clone_url'])
    return urls

def get_user_public_repos(username):
    try:
        print_delimiter()
        print("* Getting list of public repos for %s..." % username)
        r = requests.get("https://api.github.com/users/{name}/repos".format(name=username),
            params={"per_page": 10})
        print("* Get request stats: response code - {code}, content-length - {length}"
            .format(code=r.status_code,length=len(r.text)))
        clone_urls_list = get_clone_urls(r.json())
        print("* Projects list:\n\n{list}".format(list=clone_urls_list))
        print_delimiter()
        return clone_urls_list 
    except:
        print("Error occured during queriyng user public repos:")
        print(sys.exc_info())