import fileinput
import os

# Step 1 - Open the output file and replace all instances of '][' with ','. Save. 
fileToSearch = 'output.json'
outputfilename = 'final.json'
textToSearch = "]["
textToReplace = ","
if not os.path.isfile("final.json"):
	open("final.json", "w")

for line in fileinput.input(fileToSearch, inplace=True):
    print(line.replace(textToSearch, textToReplace))
  
  

# Step 2 - Open template.json and paste the contents of output.json before the end curly brace. 
inputfile = fileToSearch
with open(outputfilename,'r+') as f:
	content = open(inputfile, 'r').read()
	f.seek(0,0)
	f.write('{"interactions":' + content + '}')
	
	
#Run json2csv

os.system("python json2csv.py ./final.json ./outline.json -o ./final.csv")