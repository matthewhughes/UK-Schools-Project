import requests
import sys
import csv
import json

def GetCrimeData(latitude, longitude):
    statistics = requests.get("http://data.police.uk/api/crimes-at-location?date=2012-02&lat=" + latitude + "&lng=" + longitude).content
    print statistics

def ConvertPostCodeToLatAndLongitude(postcode):
    geodata = requests.get("http://mapit.mysociety.org/postcode/" + postcode).content
    geodata = json.loads(geodata)
    latlong = [geodata['wgs84_lat'], geodata['wgs84_lon']]
    return latlong

def main():
    print "This code will eventually do something useful"
    latlong = ConvertPostCodeToLatAndLongitude('mk181hy')
    print str(latlong[0])
    print str(latlong[1])
    GetCrimeData(str(latlong[0]), str(latlong[1]))

if __name__ == '__main__':
    main()
