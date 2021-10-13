import sys
import re

GITHUB_RAW_URL = "https://raw.githubusercontent.com/{}/main/{}"

def main():
    fileURL = sys.argv[1]
    regex = r"([^/][\w\W][^/]*)"
    result = re.findall(regex, fileURL)
    userRepo = f'{result[0]}/{result[1]}'
    fileURL = '/'.join([str(x) for x in result[2:len(result)]])
    print(GITHUB_RAW_URL.format(userRepo, fileURL))


if __name__ == "__main__":
    main()
