# dump1090-analytics

Retrieves live data from dump1090 feeds and corilates ICAO/IATA codes with airlines. The goal here is to eventually chart out the frequency of commerical, military, and private air traffic including airline data and plane types.

```bash
obihann@chickendinner:~/dump1090-analytics# /usr/bin/python3 airlines.py

VIR158 (Virgin Atlantic Airways)

Unknown Flights
['CH148810']
```

## ToDo

- store data
- find way to avoid storing duplicate data (perhaps if ICAO was seen multiple times in less than 10 minutes we can consider it a duplicate?)
- run on loop / as service
- graph data
