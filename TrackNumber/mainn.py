import phonenumbers
from Text import number
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))
