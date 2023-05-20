import urllib.request
import webbrowser

import phonenumbers
from phonenumbers import geocoder ,timezone
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
import pywhatkit

#to get the loctsation of the place through searching in google directly

number=input("Enter your number  start with country code")


#first you  have to install phone number packges pip install phonenumbers  then add geocoder  and carrier
# second opencage
testnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(testnumber,"en")

print(location)

print(carrier.name_for_number(testnumber,"en"))

key='79eafd5d45e04b799936fc2431f500fc'
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
print(result)

lat=result[1]['geometry']['lat']
lag=result[1]['geometry']['lng']

print(lat,lag)

myapp=folium.Map(location=[lat,lag], zoom_start=2)
folium.Marker([lat,lag],popup=location).add_to(myapp)
myapp.save("mylocation.html")
print(myapp)

# import pywhatkit
# pywhatkit.search("https://latitude.to/lat/"+str(lat)+"/lng/"+str(lag))
data=webbrowser.open("https://latitude.to/lat/"+str(lat)+"/lng/"+str(lag))

# print(lat, lag)
# pywhatkit.sendwhatmsg("+2556876","hellow",1,1)