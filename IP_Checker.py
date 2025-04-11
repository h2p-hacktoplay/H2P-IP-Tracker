# IP Checker from H2P
print('İts developed by H2P.')
# İnstalling required libraries (you must go to terminal and run pip install art and pip install requests.)
import requests
from art import text2art
ascii_art = text2art("H2P IP Checker")
print(ascii_art)


print('Please do not use it for illegal activities.')
print('This program is for educational purposes only.')
print('The author is not responsible for any misuse of this program.')  
print('Use it at your own risk.')
print('                                        ')

try:
    ip = requests.get("https://api.ipify.org").text
    print(f"Your IP: {ip}")
except:
    print('Error: Unable to retrieve your IP address. Please check your internet connection.')

while True:
    Ip = input('Enter the IP Address for checking: ')
    response = requests.get(f'http://ip-api.com/json/{Ip}') 
    if response.status_code == 200:
        data = response.json()
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Internet Service: {data['isp']}")
        print(f"Organisation: {data['org']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ZIP: {data['zip']}")
        print(f"Status: {data['status']}")
        print(f"Country Code: {data['countryCode']}")
        print(f"Region Code: {data['region']}")
        print(f"City Code: {data['city']}")
        print(f"ISP Code: {data['isp']}")
        print(f"Organisation Code: {data['org']}")

        google_maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
        print(f"Google Maps URL: {google_maps_url}")
    else:
        print('Error: Unable to retrieve data, Please retry.')

    # Kullanıcıya tekrar sorgu yapmak isteyip istemediğini sor
    again = input("Do you want to check another IP? (yes/no): ").strip().lower()
    if again != 'yes':
        print('Exiting the program. Developed by H2P.')
        break