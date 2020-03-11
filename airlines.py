#!/usr/bin/python3

import json
import glob
import os
import time
import datetime
import urllib.request


flights = []
unknown_codes = []
force = False
categories = {
        'A1': 'light',
        'A2': 'medium',
        'A3': 'medium',
        'A5': 'heavy',
        'A7': 'rotorcraft'
        }
iata_codes = {
        "AA": "American Airlines",
        "AC": "Air Canada",
        "RV": "Air Canada Rouge",
        "QK": "Air Canada Jazz",
        "UA": "United Airlines",
        "DL": "Delta Airlines",
        "WS": "WestJet",
        "WR": "WestJet Encore",
        "AF": "Air France",
        "DI": "Norwegian Air",
        "BA": "British Airways",
        "ZD": "Ewa Air",
        "TX": "Transportes Aéreos Nacionales",
        }
icao_codes = {
        "AAL": "American Airlines",
        "ACA": "Air Canada",
        "ROU": "Air Canada Rouge",
        "JZA": "Air Canada Jazz",
        "UAL": "United Airlines",
        "DAL": "Delta Airlines",
        "WJA": "WestJet",
        "WEN": "WestJet Encore",
        "UAE": "Emirates Airlines",
        "VLG": "Vueling Airlines",
        "TOM": "Thomson Airways",
        "TRA": "Transavia Holland",
        "UPS": "United Parcel Service",
        "TAP": "TAP Portugal",
        "TAM": "LATAM Brasil",
        "SWA": "Southwest Airlines",
        "SWG": "Sunwing Airlines",
        "RYR": "Ryanair",
        "CGE": "Nelson Aviation College",
        "AFR": "Air France",
        "EIN": "Aer Lingus",
        "KLM": "KLM",
        "IBE": "Iberia Airlines",
        "IBS": "Iberia Express",
        "JBU": "JetBlue Airways",
        "IBB": "Binter Canarias",
        "KAP": "Cape Air",
        "EZY": "easyJet",
        "IBB": "Binter Canarias",
        "HBA": "Trail Lake Flying Service",
        "AEA": "Air Europa",
        "SNC": "Air Cargo Carriers",
        "DLH": "Lufthansa",
        "GEC": "Lufthansa Cargo",
        "RCH": "Air Mobility Command",
        "EWR": "Ewa Air",
        "TAN": "Transportes Aéreos Nacionales",
        "ARL": "Airlec - Air Aquitaine Transport",
        "RRR": "UK Royal Air Force",
        "CFC": "Canadian Forces",
        "POE": "Porter Airlines",
        }

try:
    timefile = open(".lastrun")
    last_run = timefile.read()
    timefile.close()
except:
    force = True
    last_run = time.time()

raw = urllib.request.urlopen("http://192.168.0.90:8080/data/aircraft.json")
data = json.load(raw)

last_modified = data["now"]

if (float(last_run) <= float(last_modified)) or force == True:
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

timefile = open(".lastrun","w")
timefile.write(str(time.time()))
timefile.close()
