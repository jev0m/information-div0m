import requests
import pyfiglet

## By Xcode & @xcodeon1
## By Twitter : @Matrix0700
R = '\033[31m'  
G = '\033[32m'  
B = '\033[34m'  
print(R+"                        @xcodeon1")
br = pyfiglet.figlet_format("Info.py")
print(R+br)
user = input(B+"username :")
print(R+"-"*40)
url = "https://i.instagram.com:443/api/v1/users/lookup/"
cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
           "Accept-Language": "ar-AE",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
           "Accept-Encoding": "gzip, deflate"}
data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }
re = requests.post(url, headers=headers, cookies=cookies, data=data)
info = re.json()
# print(info)
print(G+"Username :"+user)
if info['email_sent'] ==  False :
     print(G+"Email_Sent : False")
else:
    print("Sms_Sent : True")
if info['sms_sent'] ==  False :
     print(G+"sms_Sent : False")
else:
    print("sms : True")
def emailPhoneIsuue(info):
    try:
        if info['obfuscated_email']:
            print(G+"His Phone Email Is : "+info['obfuscated_email'])
        else:
            pass
    except KeyError:
        'obfuscated_email'
    pass

    try:
        if info['obfuscated_phone']:
            print(G+"His Phone number Is: "+ info['obfuscated_phone'])
        else:
            print("oh")
    except KeyError:
        'obfuscated_phone'
    pass
emailPhoneIsuue(info)
print(R+"-"*40)
print("\n")