datasifter
==========

Python Script that Batch Converts and Organizes Datasift JSON Export Files from JSON to CSV


Grab your output JSON files from Datasift. Drop them all into a folder. Drop these files in the same folder. 

Navigate to your out put folder and run the python script. 

>>> "python go.py"

Watch the console for progress. It will spit out the names of each of the directories that your data dumps will be placed in (these are named for the actual hash numbers that Datasift assigned your stream/run). The end of the script will show you how many folders were created and how many files we munged. 

Email kabbott@livefyre.com if you have any questions or need help. 

Special thanks to json2csv which is used in the procressing of the compiled json files. https://github.com/evidens/json2csv
