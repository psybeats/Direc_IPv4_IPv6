#Erick Arturo Flores Gomez
#Fecha de creación: Jueves 22 de Julio 2021
#Modulo para leer la información JSON de página ipapi
#Última modificación: 
import urllib.parse
import requests
import json
import colorama
from colorama import Fore
from colorama import Style
 
def consultIP(ipaddres2):
	
	urlDirection = "https://ipapi.co/"
	json = "/json/"
	curl = urlDirection + ipaddres2 + json
	json_data = requests.get(curl).json()

	ipadd = json_data['ip']
	city = json_data['city']
	region = json_data['region']
	countryn = json_data['country_name']
	country_cap = json_data['country_capital']
	isp = json_data['org']

	printinfo = [['IP', 'Description'],
	['Your IP address is:', ipadd],
	['Your City is:', city],
	['Your State is:', region],
	['Your Country is:', countryn],
	['The capital of your country is:', country_cap],
	['Your ISP:', isp]]
	
	return printinfo

def consultIPv6api(ipaddresv6):

	countIP = ipaddresv6.count(':')

	if countIP >= 4:
	
		urlDirection = "https://ipapi.co/"
		json = "/json/"
		curl = urlDirection + ipaddresv6 + json
		json_data = requests.get(curl).json()

		ipadd = json_data['ip']
		city = json_data['city']
		region = json_data['region']
		countryn = json_data['country_name']
		country_cap = json_data['country_capital']
		isp = json_data['org']

		printinfo6 = [['IP', 'Description'],
		['Your IP address is:', ipadd],
		['Your City is:', city],
		['Your State is:', region],
		['Your Country is:', countryn],
		['The capital of your country is:', country_cap],
		['Your ISP:', isp]]

		return printinfo6
	
	else:
		error = os.system("cls")
		return error