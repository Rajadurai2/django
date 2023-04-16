import requests
def get_user_ip():
    ip=requests.get('http://ip.42.pl/raw').text
    return ip