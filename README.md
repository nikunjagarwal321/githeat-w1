#githeat-w1

##How to Run
The file "githeat-w1" can be run in command-line terminal. Beautiful soup and json library must be
installed on user's computer.

##Softwares/Tools used
1. Python 3.6
2. Beautiful Soup module(bs4)
3. json module

##What the project does
At first, we have to enter the train number whose time-table is required. The train data is
extracted using Web-Scraping (Acc. to the NTES website). The data contains train name, days of running 
and time-table(station name, arrival, departure, distance from source station). The data is stored in 
dictionary of dictionaries which is exported to a json file named "JSONData.json" in the same folder.