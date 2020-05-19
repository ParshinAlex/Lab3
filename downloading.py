from zipfile import ZipFile
import os
import requests


def download_data():
    if os.path.exists("collected_data") == 0:
        os.makedirs("collected_data")
    source = "https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip"
    response = requests.get(source)
    with open("collected_data/household_power_consumption.zip", 'wb') as file:
        for line in response:
            file.write(line)
    with ZipFile("collected_data/household_power_consumption.zip") as zipFile:
        zipFile.extractall("collected_data")
    os.remove("collected_data/household_power_consumption.zip")
