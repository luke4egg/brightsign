#!/usr/bin/env python3

import os
import sys
import http.client
import json
# import requests
#   for this implementation requests library is not used



geo_service='api.ipstack.com'


def get_geo_info(ip_address, api_key):
    """
    Get the IPStack API request for IP geolocation information.
    """
    connection = http.client.HTTPConnection(geo_service)

    url = f"http://{geo_service}/{ip_address}?access_key={api_key}"

    connection.request("GET", url)

    response = connection.getresponse()


    if response.status == 200:
        data = response.read()
        json_data = json.loads(data.decode("utf-8"))
        return json_data.get('latitude'), json_data.get('longitude')
    else:
        return None, None

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage:\n   {sys.argv[0]} <IP> [json]")
        print(f"   json is optional and indicates json output")
        sys.exit(1)

    ip_address = sys.argv[1]


    out_format = 'text'
    if len(sys.argv) == 3:
        if sys.argv[2] == 'json':
            # this if is just for basic check if second par is not malicious
            out_format = 'json'


    api_key = os.environ['IPSTACK_KEY']

    if not api_key:
        print("IPSTACK_KEY env variable is not exported")
        sys.exit(3)

       


    latitude, longitude = get_geo_info(ip_address, api_key)
  
    geo_object = {}
    geo_object['latitude'] = latitude
    geo_object['longitude'] = longitude


    if latitude and longitude:
        if out_format == 'text':
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        elif out_format == 'json':
            print(json.dumps(geo_object, indent=4))
        else:
            print("wrong output format provided")
            sys.exit(2)
    else:
        print(api_key)
        print("Failed to retrieve IP information. \nPlease check the IP address and your IPSTACK API key.")

if __name__ == "__main__":
    main()


