# git-secrets-hunter
Tool that helps to detect sensitive information in public GitHub repositories
Under the hood it uses [zricethezav/gitleaks](https://github.com/zricethezav/gitleaks) for scanning

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
