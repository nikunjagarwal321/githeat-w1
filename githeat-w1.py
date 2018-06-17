from bs4 import BeautifulSoup
import urllib.request
import json
train_no = input()
output_dictionary = []
contents_dictionary = {}
quote_page = "https://enquiry.indianrail.gov.in/xyzabc/ShowTrainSchedule?trainNo=" + train_no + "&scrnSize=&langFile=props.en-us"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
content = soup.find_all("tbody")[2]
for tr in content.find_all('tr'):
    serial_no = (tr('td')[0]).text.strip()
    station_name = (tr('td')[1]).text.strip()
    day = (tr('td')[2]).text.strip()
    arrival_time = tr.find('div', attrs = {'class' : 'm6'}).text.strip()
    departure_time = tr.find('div', attrs = {'class': 'm5'}).text.strip()
    distance = (tr('td')[4]).text.strip()
    contents_dictionary["Serial no"] = serial_no
    contents_dictionary["Station"] = station_name
    contents_dictionary["Day"] = day
    contents_dictionary["Arrival Time"] = arrival_time
    contents_dictionary["Departure Time"] = departure_time
    contents_dictionary["Distance"] = distance 
    output_dictionary.append(contents_dictionary)#Note these two lines
    print(contents_dictionary)#and this one
print(output_dictionary)#Output mein bus last element store ho raha hai baar baar

json_data = json.dumps(output_dictionary, sort_keys=True,)
with open('JSONData.json', 'w') as f:
     json.dump(json_data, f)