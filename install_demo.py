# Downloads sample data for GIS Python tutorial.  Ventura  GIS Day.
# Author: Rocky Rudolph, Channel Islands National Park, rocky_rudolph@nps.gov
# 10/28/2021

import requests, zipfile, os, sys, time


# set vars
dir_path = os.path.dirname(os.path.realpath(__file__))
destDir = r"C:\Student\GISDay_2021"
file_to_unzip = dir_path + os.sep + "GISDay2021_Python.zip"
download_file = 'https://rockne.net/files-open/VC_Python.zip'

welcome_text = """
    _____   ________________    __    __    _____   ________         
   /  _/ | / / ___/_  __/   |  / /   / /   /  _/ | / / ____/         
   / //  |/ /\__ \ / / / /| | / /   / /    / //  |/ / / __           
 _/ // /|  /___/ // / / ___ |/ /___/ /____/ // /|  / /_/ / _ _       
/___/_/ |_//____//_/ /_/  |_/_____/_____/___/_/ |_/\____(_|_|_)      
                                                                     
-- Welcome to the GIS Day 2021 Python Demo Installer --

"""


# print(dir_path)
print(welcome_text)
print("Downloading zip file {}...".format(download_file))

try:
	r = requests.get(download_file)

except:
	r = requests.get(download_file, verify=False)

open(file_to_unzip, 'wb').write(r.content)

# Bail if destination exists already.
if os.path.exists(destDir):
	sys.exit("Path " + destDir + " exists. Please manually complete the data copy processes " \
	 "to ensure that data is not being overwritten.")
	
else:
	print("Making destination directory: " + destDir)
	os.makedirs(destDir)

print("Unzipping file...")
zip_ref = zipfile.ZipFile(file_to_unzip, 'r')
zip_ref.extractall(destDir)
zip_ref.close()

print("Script done.")
print("Closing in 3 seconds")
for i in xrange(3,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)