#!/usr/bin/python3
import re, requests, time, sys, json


def plik(nazwa_pliku):
    with open(nazwa_pliku, 'r') as file:
        data = file.read()
    return data


text_str=plik("mac.txt")


def mac_extract(text_str1):
    #p = re.compile(r'(?:[0-9a-fA-F]{4}\.){2}(?:[0-9a-fA-F]{4})|(?:[0-9a-fA-F][:-]?){12}')
    p = re.compile(r'(?:[0-9a-fA-F]{4}\.){2}(?:[0-9a-fA-F]{4})|(?:[0-9a-fA-F][.:-]?){12}|(?:[0-9a-fA-F]{6}[.:-]){1}(?:[0-9a-fA-F]{6})|(?:[0-9a-fA-F]{4}[.:-]){2}(?:[0-9a-fA-F]{4})')
    extracted_mac = re.findall(p, text_str)
    return(extracted_mac)

def ip_extract(text_str1):
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    extracted_ip = re.findall(pattern, text_str)
    return(extracted_ip)


extracted=mac_extract(text_str)
extracted_ip=ip_extract(text_str)


for i in range(len(extracted)):
    time.sleep(1)
    ip = [i for i in extracted_ip]
    mac = [i for i in extracted]	     
    queryapi=requests.get(url="https://api.macvendors.com/{}".format(mac[i]))
    print("MAC: {} IP: {}, Device: {}".format(mac[i],ip[i], queryapi.content))


