from bs4 import BeautifulSoup
import urllib.request
import json

print("Enter Train number : ")
train_no = input()
output_dictionary = {}
quote_page = "https://enquiry.indianrail.gov.in/xyzabc/ShowTrainSchedule?trainNo=" + train_no + "&scrnSize=&langFile=props.en-us"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
train_name = soup.find('div', attrs={'class':'m7','class':'s9'}).text.strip()
days_of_running_div = soup.find('div', attrs ={'class' : 'm7','class' : 's11'})
days_of_running = days_of_running_div.find('span').text.strip()
output_dictionary["Train name."] = train_name
output_dictionary["Days of run"] = days_of_running
content = soup.find_all("tbody")[2]
for tr in content.find_all('tr'):
    contents_dictionary = {}
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
    output_dictionary[station_name]=contents_dictionary
    
json_data = json.dumps(output_dictionary,indent=2)
with open('JSONData.json', 'w') as f:
     json.dump(json_data, f)

print(json_data)