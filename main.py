import requests
import sys
import csv
import json

def ConvertPostCodeToLatAndLongitude(postcode):
    geodata = requests.get("http://mapit.mysociety.org/postcode/" + postcode).content
    geodata = json.loads(geodata)
    latlong = [geodata['wgs84_lat'], geodata['wgs84_lon']]
    return latlong

def main():
    print "This code will eventually do something useful"

if __name__ == '__main__':
    main()
