#!/usr/bin/env python
import requests
import json


__author__ = 'Christian Rojas'


a_url = 'http://api.open-notify.org/astros.json'
b_url = 'http://api.open-notify.org/iss-now.json'

# r = requests.get('http://api.open-notify.org/astros.json')

def get_response(url):
    if url:
        print('Response OK')
    else:
        print('Response Failed')

    
    response = requests.get(url)
    
    r_json = response.json()

    return r_json


def get_geo():
    
    """ get response """ 
    geo_response = get_response(b_url)

    """ grab response data and store """ 
    geo_arr = []
    geo_time = geo_response['timestamp']
    geo_lat = geo_response['iss_position']['latitude']
    geo_lon = geo_response['iss_position']['longitude']

    """ append response data to list """ 
    geo_arr.append(geo_time)
    geo_arr.append(geo_lat)
    geo_arr.append(geo_lon)

    return geo_arr



def main():
    astro_response = get_response(a_url)
    print get_geo()

    a_list = []
    a_count = 0

    """ loop through response and add astronauts and space craft they work on to a list """
    
    for item in astro_response['people']:
        a_list.append(item['name'] + ": " +  item['craft'])
        a_count += 1
    

    # print str(a_list) + " " + str(a_count)  


if __name__ == '__main__':
    main()
