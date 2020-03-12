#!/usr/bin/python3

import json
import glob
import os
import time
import datetime
import urllib.request
import argparse


def load_local_json(filename):
    raw = open(filename)
    data = json.load(raw)
    raw.close()
    return data

def load_dump1090_data(_server, _port, _feed):
    _url = "%s:%s/%s" % (_server, _port, _feed)

    raw = urllib.request.urlopen(_url)
    return json.load(raw)

def check_the_sky(url, port="8080", feed="data/aircraft.json", force = False):
    flights = []
    known_flights = []
    unknown_codes = []
    last_run = time.time()
    # now = time.time()
    now_string = time.strftime("%c %T")
    working_dir = os.path.abspath(os.path.dirname(__file__))
    icao_codes = load_local_json("%s/%s" % (working_dir, "./data/icao.json"))
    iata_codes = load_local_json("%s/%s" % (working_dir, "./data/iata.json"))
    data = load_dump1090_data(url, port, feed)

    try:
        timefile = open(".lastrun", "r")
        last_run = timefile.read()
        timefile.close
    except:
        _force = True

    if (float(last_run) <= float(data["now"])) or force == True:
        flights = [obj["flight"].strip() for obj in data["aircraft"] if "flight" in obj]
        flights = list(dict.fromkeys(flights))
        flights = sorted(flights)

        for flight in flights:
            if flight[0:3] in icao_codes:
                known_flights.append("%s (%s) (Last seen: %s)" % (flight, icao_codes[flight[0:3]], now_string))
            elif flight[0:2] in iata_codes:
                known_flights.append("%s (%s) (Last seen: %s)" % (flight, iata_codes[flight[0:2]], now_string))
            else:
                unknown_codes.append(flight)

    if known_flights != []:
        print("Flights:\n%s" % '\n'.join(known_flights))

    if unknown_codes != []:
        print("\nUnknown:\n%s" % '\n'.join(unknown_codes))

    timefile = open(".lastrun", "w")
    timefile.write(str(time.time()))
    timefile.close()