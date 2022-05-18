#this imports the package 'csv' which is from the python Standard Library
import csv

#this import is local and outside the scope of the tutorial, but PANOS exports CSV files with a BOM and it needs
#to be removed
from remove_bom import remove_bom_inplace

remove_bom_inplace("sample_zones.csv")


#this line of code will open the CSV file as the variable 'file'.
#there are other ways to open a file, but using 'with' will close the file once all the code within the "with'
#is complete.
#notice the 'r' argument provided after the filename, this means the file will be opened as read
#more on python and files https://www.pythontutorial.net/python-basics/python-read-text-file/

with open("sample_zones.csv","r") as file:
    #this will open the file into a csv.DictReader object which uses the headers of the CSV to create a dictionary
    #the 'rows' object is the name of the csv.DictReader
    rows = csv.DictReader(file)
    #'zones' is a simple list object that we will then append each row onto and create a list of dictionaries
    zones = []
    #this will iterate over the 'rows' object and append each row to the list called 'zones'
    #the 'row' object is each item from rows as it iterates, so each pass of the loop, the row actually changes to the next
    for row in rows:
        zones.append(row)

#Now that we have a list of dictionaries to work with we can generate some commands
#In this situation, we want to add a zone protection to each zone called 'Recommended_Zone_Protection'

#this is a simple set command for palo alto PANOS, this command was pulled from the firewall CLI
#the cmd object is a string, which is a group of characters
#notice the curly brackets in the command, this will allow you to use '.format' function
cmd = "set zone {} network zone-protection-profile Recommended_Zone_Protection"

#next we will print this command for each zone and insert the name via the curly brackets and format function

#this is another loop that will iterate over each zone in the list of zones
for zone in zones:

    #a new variable is made for the zone name
    #the zone object is a dictionary created from the CSV and thus needs a key to get the value
    #to get a value from a dictionary use this syntax; object['key']
    zone_name = zone['Name']

    #finally we will print the command and format the command to include the zone name
    print(cmd.format(zone_name))