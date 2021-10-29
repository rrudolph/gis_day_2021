# Downloads sample data for GIS Python tutorial.  Ventura  GIS Day.
# Author: Rocky Rudolph, Channel Islands National Park, rocky_rudolph@nps.gov
# 10/28/2021

import requests, zipfile, os, sys, time

def download_url(url, save_path, chunk_size=128):
	print("Starting download")
	r = requests.get(url, stream=True)
	print(r)
	with open(save_path, 'wb') as fd:
		for chunk in r.iter_content(chunk_size=chunk_size):
			fd.write(chunk)


# set vars
dir_path = os.path.dirname(os.path.realpath(__file__))
destDir = r"C:\Student\GISDay_2021_test"
file_to_unzip = os.path.join(dir_path, "GISDay2021_Python.zip")
download_file = 'https://github.com/rrudolph/gis_day_2021/raw/main/GIS_Day_2021.zip'

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

download_url(download_file, file_to_unzip)

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
for i in range(3,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)
