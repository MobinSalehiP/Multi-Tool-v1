import requests
import os
import json

logo = """
  __  __      _ _   _   _____         _       ___ 
 |  \/  |_  _| | |_(_) |_   _|__  ___| | __ _| __|
 | |\/| | || | |  _| |   | |/ _ \/ _ \ | \ V /__ \\
 |_|  |_|\_,_|_|\__|_|   |_|\___/\___/_|  \_/|___/
"""

while True:
    os.system("title Multi Tool v5 ")
    os.system("cls")
    print(logo)
    print("[1]Ip lookup")
    print("[2]Webhook Sender")
    print("[3]Show SDID")
    print("")
    x = input("Option : ")

    if x == "1":
        os.system("cls")
        print("Ip lookup\n")
        ip = input("Enter Ip : ")

        
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()

        print("RESULTS\n")

        
        print(f"Status : {data['status']}")
        print(f"Country : {data['country']}")
        print(f"City : {data['city']}")
        print(f"Region : {data['regionName']}")
        print(f"TimeZone : {data['timezone']}")
        print(f"ISP : {data['isp']}")
        print("")
        pause = input("press enter to return...")

    if x == "2":
        os.system("cls")
        print("Webhook Sender\n")
        url = input("webhook url : ")
        message = input("message : ")
        name = input("webhook name : ")

        
        data = {
            "content": message,
            "username": name
        }

        try:
            requests.post(url, json=data)
            print("WEBHOOK SENT")
        except:
            print("ERROR SENDING WEBHOOK")

        print()
        pause = input("press enter to return...")

    if x == "3":
        os.system("cls")
        print("SDID\n")

        
        print("CPU SERIAL")
        os.system("wmic cpu get ProcessorId")

        print("DISK SERIAL")
        os.system("wmic diskdrive get SerialNumber")

        print("OTHER BOARD SERIAL")
        os.system("wmic baseboard get SerialNumber")

        print()
        pause = input("press enter to return...")

    else:
        os.system("cls")
        print("invalid Option")
