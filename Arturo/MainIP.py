#Erick Arturo Flores Gomez
#Fecha de creación: Jueves 22 de Julio 2021
#Menú para ingresar direcciones IP, detenciones abrutpas y comprovación de direcciones
#Última modificación: Viernes 23 de Julio 2021
import urllib.parse
import requests
import os
import colorama
from colorama import Fore
from colorama import Style
from tabulate import tabulate
from datetime import date
from datetime import datetime

import ipstack as stack
import ipapi as api
import classforAPI as clApi

print(Fore.GREEN + "=*="*20 + Style.RESET_ALL)
print(Fore.CYAN + Style.BRIGHT +"Informative application of public IPv4 and IPv6 addresses" + Style.RESET_ALL )
print(Fore.GREEN + "=*="*20 + Style.RESET_ALL)

try:
	while True:
		print(Fore.RED + Style.BRIGHT + "Select an API to work" + Style.RESET_ALL) 
		print(Fore.MAGENTA + Style.BRIGHT + "1. IPstack \n" +
			  "2. IPapi \n" +
			  "0. Exit \n" +
			  "Choose an option: " + Style.RESET_ALL)
		user_decision = input()
### SELECCIONO IPSTACK - SELECCIONAR ENTRE IPv4 E IPv6 ***********************************************************
		if user_decision == '1':
			print(Fore.GREEN + Style.NORMAL + "=*="*20 + Style.RESET_ALL)
			print(Fore.YELLOW + Style.BRIGHT + "Press Enter twice to return to the menu" + Style.RESET_ALL)
			print(Fore.RED + Style.NORMAL + "Select the type of IP" + Style.RESET_ALL)
			print(Fore.BLUE + Style.NORMAL + "1. IPv4\n" + 
				  	"2. IPv6\n" +
			  		"\nChoose an option: " + Style.RESET_ALL)
			user_decision_type = input()
			
### SELECCIONAR LA OPCION NUMERO 1, IPv4 PARA IPSTACK ------------------------------------------------------------
			if user_decision_type == '1':
				try:
					nameAPI = "IPstack"
					print(Fore.RED + Style.NORMAL + "Please enter an IP address: " + Style.RESET_ALL)
					ipaddres = input()

					ip1 = stack.consultIPstack(ipaddres)

					print(Fore.CYAN + "=*="*21 + Style.RESET_ALL)
					print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + tabulate(ip1, headers='firstrow', tablefmt='grid') + Style.RESET_ALL)
					print(Fore.CYAN + "=*="*21 + Style.RESET_ALL)

					typeip = clApi.typeAPI(ipaddres)
					print_typeIP= typeip.yourIP_is_ipv4()
					print_rangeIP = typeip.rangeIPv4()

					print(print_typeIP + "\n" + print_rangeIP)

					print("Your API used was: " + nameAPI)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)
				except:
					os.system("cls")
					print(Fore.RED + Style.NORMAL + "Wrong value, try again!!!" + Style.RESET_ALL)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)

### SELECCIONAR LA OPCION NUMERO 2, IPv6 PARA IPSTACK ------------------------------------------------------------
			elif user_decision_type == '2':
				try:
					nameAPI = "IPstack"
					print(Fore.RED + Style.NORMAL + "Please enter an IP address: " + Style.RESET_ALL)
					ipaddres = input()

					ip1 = stack.consultIPv6stack(ipaddres)

					print(Fore.CYAN + "=*="*21 + Style.RESET_ALL)
					print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + tabulate(ip1, headers='firstrow', tablefmt='grid') + Style.RESET_ALL)
					print(Fore.CYAN + "=*="*21 + Style.RESET_ALL)

					print("Your API used was: " + nameAPI)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)
				except:
					os.system("cls")
					print(Fore.RED + Style.NORMAL + "Wrong value, try again!!!" + Style.RESET_ALL)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)

### SELECCIONO IPAPI - SELECCIONAR ENTRE IPv4 E IPv6 ***********************************************************
		elif user_decision == '2':
			print(Fore.GREEN + Style.NORMAL + "=*="*20 + Style.RESET_ALL)
			print(Fore.YELLOW + Style.BRIGHT + "Press Enter twice to return to the menu" + Style.RESET_ALL)
			print(Fore.RED + Style.NORMAL + "Select the type of IP" + Style.RESET_ALL)
			print(Fore.BLUE + Style.NORMAL + "1. IPv4\n" + 
				  "2. IPv6" + Style.RESET_ALL)
			user_decision_ipapi = input()
### SELECCIONAR LA OPCION NUMERO 1, IPv4 PARA IPAPI ------------------------------------------------------------
			if user_decision_ipapi == '1':
				try:
					nameAPI = "IPapi"
					print(Fore.RED + Style.NORMAL + "Please enter an IP address: " + Style.RESET_ALL)
					ipaddres2 = input()

					ip2 = api.consultIP(ipaddres2)

					print(Fore.CYAN + "=*="*24 + Style.RESET_ALL)
					print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + tabulate(ip2, headers='firstrow', tablefmt='grid') + Style.RESET_ALL)
					print(Fore.CYAN + "=*="*24 + Style.RESET_ALL)

					typeip = clApi.typeAPI(ipaddres2)
					print_typeIP= typeip.yourIP_is_ipv4()
					print_rangeIP = typeip.rangeIPv4()

					print(print_typeIP + "\n" + print_rangeIP)

					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)
				except:
					os.system("cls")
					print(Fore.RED + Style.NORMAL + "Wrong value, try again!!!" + Style.RESET_ALL)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)

### SELECCIONAR LA OPCION NUMERO 2, IPv6 PARA IPSTACK ------------------------------------------------------------
			elif user_decision_ipapi == '2':
				try:
					nameAPI = "IPapi"
					print(Fore.RED + Style.NORMAL + "Please enter an IP address: " + Style.RESET_ALL)
					ipaddres2 = input()

					ip2 = api.consultIPv6api(ipaddres2)

					print(Fore.CYAN + "=*="*24 + Style.RESET_ALL)
					print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + tabulate(ip2, headers='firstrow', tablefmt='grid') + Style.RESET_ALL)
					print(Fore.CYAN + "=*="*24 + Style.RESET_ALL)

					typeip = clApi.typeAPI(ipaddres2)

					print("Your API used was: " + nameAPI)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)
				except:
					os.system("cls")
					print(Fore.RED + Style.NORMAL + "Wrong value, try again!!!" + Style.RESET_ALL)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)

###OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
		elif user_decision > '2':
			print(Fore.RED + Style.BRIGHT + "Wrong value, try again!!!" + Style.RESET_ALL)
			print(Fore.GREEN + Style.BRIGHT + "Press enter to return to the menu!!!" + Style.RESET_ALL)
###OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
		elif user_decision == '0':
			os.system("cls")
			print(Fore.RED + "The program ended" + Style.RESET_ALL)
			print(Fore.YELLOW + "Thank you for using this program" + Style.RESET_ALL)
			break

		input()
		os.system("cls")

except Exception as e:
    print(f'\n{e}')

finally:
	now = datetime.now()
	format = now.strftime('%A %B %d, %Y - %I:%M%p')

	print(Fore.GREEN + Style.BRIGHT + "Developer name: Erick Arturo Flores Gomez" + Style.RESET_ALL)
	print(Fore.GREEN + Style.BRIGHT + "Project creation date: Thursday July 22, 2021." + Style.RESET_ALL)
	print(Fore.GREEN + "The end date and time is: " + format + Style.RESET_ALL)