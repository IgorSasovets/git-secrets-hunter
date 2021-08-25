# git-secrets-hunter
Tool that helps to detect sensitive information in public GitHub repositories

## Features
* Scan a user repository using [zricethezav/gitleaks](https://github.com/zricethezav/gitleaks) tool
* Scan a user repository using [truffleHog](https://github.com/trufflesecurity/truffleHog) tool
* Automatically install [zricethezav/gitleaks](https://github.com/zricethezav/gitleaks) binary depending on you OS
* Read list of usernames for scanning from a file
* Get public repositories of the user

## Usage

```
:'######:::'####:'########:
'##... ##::. ##::... ##..::
 ##:::..:::: ##::::: ##::::
 ##::'####:: ##::::: ##::::
 ##::: ##::: ##::::: ##::::
 ##::: ##::: ##::::: ##::::
. ######:::'####:::: ##::::
:......::::....:::::..:::::
:'######::'########::'######::'########::'########:'########::'######::
'##... ##: ##.....::'##... ##: ##.... ##: ##.....::... ##..::'##... ##:
 ##:::..:: ##::::::: ##:::..:: ##:::: ##: ##:::::::::: ##:::: ##:::..::
. ######:: ######::: ##::::::: ########:: ######:::::: ##::::. ######::
:..... ##: ##...:::: ##::::::: ##.. ##::: ##...::::::: ##:::::..... ##:
'##::: ##: ##::::::: ##::: ##: ##::. ##:: ##:::::::::: ##::::'##::: ##:
. ######:: ########:. ######:: ##:::. ##: ########:::: ##::::. ######::
:......:::........:::......:::..:::::..::........:::::..::::::......:::
'##::::'##:'##::::'##:'##::: ##:'########:'########:'########::
 ##:::: ##: ##:::: ##: ###:: ##:... ##..:: ##.....:: ##.... ##:
 ##:::: ##: ##:::: ##: ####: ##:::: ##:::: ##::::::: ##:::: ##:
 #########: ##:::: ##: ## ## ##:::: ##:::: ######::: ########::
 ##.... ##: ##:::: ##: ##. ####:::: ##:::: ##...:::: ##.. ##:::
 ##:::: ##: ##:::: ##: ##:. ###:::: ##:::: ##::::::: ##::. ##::
 ##:::: ##:. #######:: ##::. ##:::: ##:::: ########: ##:::. ##:
..:::::..:::.......:::..::::..:::::..:::::........::..:::::..::
    
usage: git-secrets-hunter.py [-h] [-f FILE] [-u USERNAME] [-m MODE] [-p PLATFORM]

Git secrets hunter options:

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path of a file that contains list of GitHub usernames
  -u USERNAME, --username USERNAME
                        GitHub username of a target
  -m MODE, --mode MODE  run mode. Available modes: ['scan_single_user', 'scan_list_of_users']
  -p PLATFORM, --platform PLATFORM
                        OS platform (for gitleaks), available platforms: ['linux-amd64', 'linux-arm', 'linux-mips', 'darwin-
                        amd64', 'windows-386.exe', 'windows-amd64.exe']

```

## TODO:
- [ ] Integrate [semgrep](https://github.com/returntocorp/semgrep) tool
- [ ] Extend number of available options
- [ ] Add possibility to save program output into a file

## Examples

### Scan repositories of a single GitHub user
```
python3 git-secrets-hunter.py -u IgorSasovets -m scan_single_user -p linux-amd64
```
### Scan multiple users repositories

At first, you should create file with list of GitHub users to scan

users.txt
```
IgorSasovets
```
Then, launch scan using the `scan_list_of_users` mode
```
python3 git-secrets-hunter.py -f users.txt -p linux-amd64 -m scan_list_of_users
```
