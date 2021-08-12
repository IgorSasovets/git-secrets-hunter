from pathlib import Path

GITLEAKS_PLATFORMS_LIST = ["linux-amd64", "linux-arm", "linux-mips", "darwin-amd64",
    "windows-386.exe", "windows-amd64.exe"]
GITLEAKS_BINARY_PATH = str(Path.cwd()) + "/gitleaks-binary/gitleaks"
GITLEAKS_DOWNLOAD_URL = "https://github.com/zricethezav/gitleaks/releases/download/v7.5.0/gitleaks-"
GITLEAKS_SCAN_DEPTH = 100
TRUFFLEHOG_SCAN_DEPTH = 50
TRUFFLEHOG_EXCLUDE_PATTERNS_PATH = str(Path.cwd()) + "/truffle_hog_patterns/common_exclude_patterns.txt"
SCANNERS_LIST = ["all", "gitleaks", "truffleHog"]