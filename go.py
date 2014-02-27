import csv
import glob
import os
import json
from collections import OrderedDict
import fileinput

# Lets glob these mofos
files = glob.glob( '*.json' )

# If the archive directory doesn't exist, create it. That's where we will dump files after we're doing reading them.
if not os.path.exists("archive"):
    os.makedirs("archive")

# Declaring an array of the output directories we're creating. Empty for now. 
directory_listing = []

# File counter (for logging)
count = 0

# Loop through the files and do....
for f in files:
  # Load the Json into J
  j = json.load(open(f))
  # Load the interactions node (and all its contents) into jdump
  jdump = json.dumps(j['interactions'])
  # Load the hash value into a variable called 'folder'
  folder = j['hash']
  # Check to see if a folder with the hash value exists. If it doesn't create it.
  if not os.path.exists(folder):
    os.makedirs(folder)
    directory_listing.append(folder)
  # We're going to store our output into a new file in that folder called 'output.json'
  filename = 'output.json'
  with open(os.path.join(folder, filename), 'a') as file:
  	file.write(jdump)
  #Now move that file from the current directory to the archive (just some helpful housekeeping here)
  os.rename(f,"./archive/"+f)
  #Repeat for every file in the glob
  count += 1

#Now loop through the directories
for item in directory_listing:
  print item
  # Step 1 - Open the output file and replace all instances of '][' with ','. Save. 
  fileToSearch = item+'/output.json'
  outputfilename = item+'/final.json'
  textToSearch = "]["
  textToReplace = ","
  if not os.path.isfile(item+"/final.json"):
  	open(item+"/final.json", "w")

  for line in fileinput.input(fileToSearch, inplace=True):
    print(line.replace(textToSearch, textToReplace))

  # Step 2 - Open template.json and paste the contents of output.json before the end curly brace. 
  inputfile = fileToSearch
  with open(outputfilename,'r+') as f:
	content = open(inputfile, 'r').read()
	f.seek(0,0)
	f.write('{"interactions":' + content + '}')

  #Run json2csv
  os.system("python ./processfiles/json2csv.py ./"+outputfilename+" ./processfiles/outline.json -o ./"+item+"/final.csv")

print("Directory Listing has "+str(len(directory_listing))+" values in it.")
print("File count: "+str(count))
