#Erick Arturo Flores Gomez
#Fecha de creación: Jueves 22 de Julio 2021
#Menú para ingresar direcciones IP, detenciones abrutpas y comprovación de direcciones
#Última modificación: Viernes 23 de Julio 2021
import urllib.parse
import requests
import os
from colorit import *
import colorama
from colorama import Fore
from colorama import Style
from tabulate import tabulate
from datetime import date
from datetime import datetime

import ipstack as stack
import ipapi as api
import classforAPI as clApi


try:
	while True:
		print(color("=*="*20, (224, 242, 241)))
		print(color("Informative application of public IPv4 and IPv6 addresses",(255, 255, 0)), end=""),
		print(color(" ||", (224, 242, 241)))

		print(color("=*="*20, (224, 242, 241)))
		print(Fore.RED + Style.BRIGHT + "Select an API to work\t\t\t\t\t " + Style.RESET_ALL, end=""),
		print(color(" ||", (224, 242, 241)))
		print(color("=*="*20, (224, 242, 241)))

		print(color("1. IPstack \n" +
			  "2. IPapi \n" +
			  "0. Exit \n" +
			  "Choose an option: ", (3, 169, 244)))
		user_decision = input()
### SELECCIONO IPSTACK - SELECCIONAR ENTRE IPv4 E IPv6 ***********************************************************
		if user_decision == '1':

			os.system("cls")

			
			print(color("Press Enter twice to return to the menu", (255, 179, 0)))

			print(color("=*="*20, (224, 242, 241)))
			print(Fore.RED + Style.BRIGHT + "Select the type of IP\t\t\t\t\t " + Style.RESET_ALL, end=""),
			print(color(" ||", (224, 242, 241)))
			print(color("=*="*20, (224, 242, 241)))
			print(color("1. IPv4\n" + "2. IPv6\n" + "Choose an option: ", (3, 169, 244)))
			
			user_decision_type = input()
			
### SELECCIONAR LA OPCION NUMERO 1, IPv4 PARA IPSTACK ------------------------------------------------------------
			if user_decision_type == '1':
				try:
					nameAPI = "IPstack"
					print(Fore.RED + Style.NORMAL + "Please enter an IP address: " + Style.RESET_ALL)
					ipaddres = input()

					ip1 = stack.consultIPstack(ipaddres)

					print(color("=*="*24, (224, 242, 241)))
					print(color(tabulate(ip1, headers='firstrow', tablefmt='grid'), (255, 235, 59)))
					print(color("=*="*24, (224, 242, 241)))

					typeip = clApi.typeAPI(ipaddres)
					print_typeIP= typeip.yourIP_is_ipv4()
					print_rangeIP = typeip.rangeIPv4()

					print(print_typeIP + "\t\t\t\t\t\t      ",end=""),
					print("||")
					print(print_rangeIP + "\t\t\t       ",end=""),
					print("*")
					print("Your API used was: " + nameAPI + "\t\t\t\t\t      ",end=""),
					print("||")
					print(color("=*="*24, (224, 242, 241)))

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

					print(color("=*="*21, (224, 242, 241)))
					print(color(BRIGHT + tabulate(ip1, headers='firstrow', tablefmt='grid'), (255, 235, 59)))
					print(color("=*="*21, (224, 242, 241)))

					print("Your API used was: " + nameAPI)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)
				except:
					os.system("cls")
					print(Fore.RED + Style.NORMAL + "Wrong value, try again!!!" + Style.RESET_ALL)
					print(Fore.GREEN + Style.BRIGHT + "\nPress enter to return to the menu!!!" + Style.RESET_ALL)

### SELECCIONO IPAPI - SELECCIONAR ENTRE IPv4 E IPv6 ***********************************************************
		elif user_decision == '2':
			os.system("cls")

			
			print(color("Press Enter twice to return to the menu", (255, 179, 0)))

			print(color("=*="*20, (224, 242, 241)))
			print(Fore.RED + Style.BRIGHT + "Select the type of IP\t\t\t\t\t " + Style.RESET_ALL, end=""),
			print(color(" ||", (224, 242, 241)))
			print(color("=*="*20, (224, 242, 241)))
			print(color("1. IPv4\n" + "2. IPv6\n" + "Choose an option: ", (3, 169, 244)))
			
			user_decision_ipapi = input()
### SELECCIONAR LA OPCION NUMERO 1, IPv4 PARA IPAPI ------------------------------------------------------------
			if user_decision_ipapi == '1':
				try:
					nameAPI = "IPapi"
					print(Fore.RED + Style.NORMAL + "Please enter an IP address: " + Style.RESET_ALL)
					ipaddres2 = input()

					ip2 = api.consultIP(ipaddres2)

					print(color("=*="*24, (224, 242, 241)))
					print(color(tabulate(ip2, headers='firstrow', tablefmt='grid'), (255, 235, 59)))
					print(color("=*="*24, (224, 242, 241)))

					typeip = clApi.typeAPI(ipaddres2)
					print_typeIP= typeip.yourIP_is_ipv4()
					print_rangeIP = typeip.rangeIPv4()


					print(print_typeIP + "\t\t\t\t\t\t      ",end=""),
					print("||")
					print(print_rangeIP + "\t\t\t       ",end=""),
					print("*")
					print("Your API used was: "  + nameAPI + "\t\t\t\t\t      ",end=""),
					print("||")
					print(color("=*="*24, (224, 242, 241)))

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

					print(color("=*="*24, (224, 242, 241)))
					print(color(tabulate(ip2, headers='firstrow', tablefmt='grid'), (255, 235, 59)))
					print(color("=*="*24, (224, 242, 241)))

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

			now = datetime.now()
			date = now.strftime('%A %B %d, %Y')
			time = now.strftime('%I:%M%p')

			print(color("Developer name: Erick Arturo Flores Gomez",(51, 255, 0)))
			print(color("Project creation date: Thursday July 22, 2021.",(51, 255, 102)))
			print(color("The end date is: " + date + " and the time is: " + time, (51, 255, 102)))
			break

		input()
		os.system("cls")

except Exception as e:
    print(f'\n{e}')

finally:
	print(color("The program ended", (255, 0, 0)))
	print(color("Thank you for using this program", (255, 204, 0)))
