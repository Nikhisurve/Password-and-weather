import speech_recognition as sr #pip install speechRecognition
import webbrowser
import pywhatkit as kt
from requests_html import HTMLSession



#have used ubantu os


#print("enter the city name")
#query=input()
#webbrowser.open("https://www.google.com/search?q=weather "+query)

s=HTMLSession()

content=input("enter the city name\n")
query=content
url=f'https://www.google.com/search?q=weather +{query}'

r=s.get(url,headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

Temp=r.html.find('span#wob_tm',first=True).text
Unit=(r.html.find('div.vk_bk.wob-unit span.wob_t',first=True)).text
Discription=(r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True)).text

print("City:",query,Temp,Unit)
print(Discription)



