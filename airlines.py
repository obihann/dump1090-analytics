#!/usr/bin/python3

import json
import glob
import os
import time
import datetime
import urllib.request


def load_local_json(filename):
    raw = open(filename)
    data = json.load(raw)
    raw.close()
    return data

def load_dump1090_data():
    raw = urllib.request.urlopen("http://192.168.0.90:8080/data/aircraft.json")
    return json.load(raw)

def main():
    flights = []
    unknown_codes = []
    force = False
    categories = load_local_json("./data/categories.json")
    icao_codes = load_local_json("./data/icao.json")
    iata_codes = load_local_json("./data/iata.json")
    data = load_dump1090_data()

    try:
        timefile = open(".lastrun", "r")
        last_run = timefile.read()
        timefile.close
    except:
        force = True
        last_run = time.time()

    if (float(last_run) <= float(data["now"])) or force == True:
        for obj in data["aircraft"]:
            if "flight" in obj:
                flight = obj["flight"].strip()
                flights.append(flight)

        flights = list(dict.fromkeys(flights))
        flights = sorted(flights)

        for flight in flights:
            if flight[0:3] in icao_codes:
                print("%s (%s)" % (flight, icao_codes[flight[0:3]]))
            else:
                if flight[0:2] in iata_codes:
                    print("%s (%s)" % (flight, iata_codes[flight[0:2]]))
                else:
                    unknown_codes.append(flight)

    if unknown_codes != []:
        print("\nUnknown Flights")
        print(unknown_codes)


    timefile = open(".lastrun", "w")
    timefile.write(str(time.time()))
    timefile.close()

main()