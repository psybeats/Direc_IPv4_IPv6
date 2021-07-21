# Alejandro Alan Gutierrez Cortes, Mie, 21/07/2021, Aplicación Informativa de direcciones IPv4 e IPv6 públicas.

import requests
import json
import os
import datetime
import socket
import urllib.request


def get_private_ip():
    try:
        hostname = socket.gethostname()
        ip_address_v4 = socket.gethostbyname(hostname)
        ip_address_v6 = socket.gethostbyaddr(hostname)
        list_ip_address_v6 = ip_address_v6
        ip_address2 = socket.getaddrinfo("google.com", 80)
        print(f'\nMy Hostname is: {hostname}')
        print('My Internal Ipv4 Address is: {} '.format(ip_address_v4))
        print('My Internal Ipv6 Address is: {} '.format("".join(list_ip_address_v6[2])))
        print(f'Google Ip Address is: {ip_address2}')
        return
        pass
    except Exception as e:
        print(e)
    finally:
        pass


def get_public_ip():
    try:
        external_ipv4 = urllib.request.urlopen('https://v4.ident.me/').read( ).decode('utf8')
        print(f'My Public Ipv4 Address is: {external_ipv4}')
        external_ipv6 = urllib.request.urlopen('https://ident.me/').read().decode('utf8')
        print(f'My Public Ipv6 Address is: {external_ipv6}\n')
        return
        pass
    except Exception as e:
        print(e)
    finally:
        pass


def menu():
    try:
        print('Bienvenido al software 🎈 seleccione una opción del siguiente menú:')
        options = ['IpStack', 'IpAPI', 'Salir']
        print(f'\t1 ➡ {options[0]}')
        print(f'\t2 ➡ {options[1]}')
        print(f'\t3 ➡ {options[2]}')
        return
        pass
    except Exception as e:
        print(e)
    finally:
        pass


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_json_info_ipstack(ip, key):
    try:
        full_link = "http://api.ipstack.com/"
        url = full_link + ip + "?access_key=" + key
        str_obj01 = requests.get(url).json()
        current_time01 = datetime.datetime.now()
        time_format01 = current_time01.strftime('[%d-%m-%y]_[%Ihrs %Mmin]')
        path, _ = os.path.split(os.path.abspath(__file__))
        with open(path + '/LOG_DATA_API_IPSTACK_' + time_format01 + '.json', 'a', encoding='utf8') as file:
            json.dump(str_obj01, file, indent=4)
            #json.dump(str_obj01, file, indent=4, separators=(".", " = "), sort_keys=True)
        return str_obj01
    except Exception as e:
        print(e)
    finally:
        pass


def get_json_info_ipapi(ip2, format01):
    try:
        full_link2 = "https://ipapi.co/"
        curl = full_link2 + ip2 + format01
        str_obj02 = requests.get(curl).json()
        current_time02 = datetime.datetime.now()
        time_format02 = current_time02.strftime('[%d-%m-%y]_[%Ihrs %Mmin]')
        path, _ = os.path.split(os.path.abspath(__file__))
        with open(path + '/LOG_DATA_API_IPAPI_' + time_format02 + '.json', 'a', encoding='utf8') as file:
            json.dump(str_obj02, file, indent=4)
            #json.dump(str_obj02, file, indent=4, separators=(".", " = "), sort_keys=True)
        return str_obj02
    except Exception as e2:
        print(e2)
    finally:
        pass
