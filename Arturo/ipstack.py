#Erick Arturo Flores Gomez
#Fecha de creación: Jueves 22 de Julio 2021
#Clase para leer la información JSON de la página ipstack
#Última modificación: 

import urllib.parse
import requests
import json

def consultIPstack(ipaddress1):
	urlDirection = "http://api.ipstack.com/"
	access_key = "0f112a9d7cc006d5792934447641a66f"
	curl = urlDirection + ipaddress1 + "?access_key=" + access_key
	json_data_stack = requests.get(curl).json()



	ipadd = json_data_stack['ip']
	city = json_data_stack['city']
	region = json_data_stack['region_name']
	countryn = json_data_stack['country_name']
	capital_c = json_data_stack['location']['capital']

	printinfo = [['IP', 'Description'],
	['Your IP address is:', ipadd],
	['Your City is:', city],
	['Your State is:', region],
	['Your Country is:', countryn],
	['The capital of your country is:', capital_c]]

	return printinfo

def consultIPv6stack(ipaddressv6):

	countIP = ipaddresv6.count(':')

	if countIP >= 4:
		urlDirection = "http://api.ipstack.com/"
		access_key = "0f112a9d7cc006d5792934447641a66f"
		curl = urlDirection + ipaddressv6 + "?access_key=" + access_key
		json_data_stack = requests.get(curl).json()

		ipadd = json_data_stack['ip']
		city = json_data_stack['city']
		region = json_data_stack['region_name']
		countryn = json_data_stack['country_name']
		capital_c = json_data_stack['location']['capital']

		printinfo = [['IP', 'Description'],
		['Your IP address is:', ipadd],
		['Your City is:', city],
		['Your State is:', region],
		['Your Country is:', countryn],
		['The capital of your country is:', capital_c]]

		return printinfo

	else:
		error = os.system("cls")
		return error