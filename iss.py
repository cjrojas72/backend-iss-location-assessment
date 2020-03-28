#!/usr/bin/env python
import requests
import json
import turtle
import threading


__author__ = 'Christian Rojas'

a_url = 'http://api.open-notify.org/astros.json'
b_url = 'http://api.open-notify.org/iss-now.json'

map_img = 'map.gif'
iss_img = 'iss.gif'

s = turtle.getscreen()
t = turtle.Turtle()


# screen.bgpic(map_img)

def set_cord():
    threading.Timer(1.0, set_cord).start()
    pos = get_geo()
    x_cord = pos[1]
    y_cord = pos[2]
    
    x_cord = float(x_cord)
    y_cord = float(y_cord)

    t.goto(x_cord,y_cord)

    return "hi"
    

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
    s.bgpic(map_img)
    s.addshape(iss_img)
    t.shape(iss_img)

    set_cord()

    # x_cord = init_pos[1]
    # y_cord = init_pos[2]
    
    # x_cord = float(x_cord)
    # y_cord = float(y_cord)

    # t.goto(x_cord,y_cord)
    s.exitonclick()
    threading.Timer(set_cord).cancel()


    astro_response = get_response(a_url)

    a_list = []
    a_count = 0

    """ loop through response and add astronauts and space craft they work on to a list """
    
    for item in astro_response['people']:
        a_list.append(item['name'] + ": " +  item['craft'])
        a_count += 1
    

    # print str(a_list) + " " + str(a_count)  


if __name__ == '__main__':
    main()
