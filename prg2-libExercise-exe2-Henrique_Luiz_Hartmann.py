import smtplib
import getpass
import requests
from pprint import pprint

r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Araquari,br&APPID=24e5518adced091b9c6413f750c7bec7')
rain = r.json()['list'][0]['weather'][0]['description']
string = ''
if 'rain' in rain:
    string = 'tomorow will rain'
else:
    string = 'tomorow will not rain'
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('joaosilvapires3@gmail.com', 'SenhaGmail_5@')
smtpObj.sendmail('joaosilvapires3@gmail.com', 'red.deutsch23@gmail.com', 'Subject: {}'.format(string))