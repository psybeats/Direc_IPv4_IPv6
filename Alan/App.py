# Alejandro Alan Gutierrez Cortes, Mie, 21/07/2021, Aplicación Informativa de direcciones IPv4 e IPv6 públicas.

import Def as misfunciones
import Model as miclase
import pandas as pd
import numpy as np
from colorit import *
from colorama import Fore, init
from termcolor import colored


# * Inicializa imprimir en la consola a color
init()
init_colorit()


print(Fore.MAGENTA, '\n\t🛑 INFO IMPORTANTE 🛑')

misfunciones.get_private_ip()
misfunciones.get_public_ip()

print(color('🍀 Inicio del software 🍀', Colors.red))
print(Fore.BLUE)

try:
    while not False:
        misfunciones.menu()
        decision = None
        user_Decision = input(f'\nIngrese una opción >>\t')
        misfunciones.clear_console()
        if user_Decision == '1':
            decision = 'IpStack'
            consult_api01 = miclase.Api01(
                '318ad030e610126d41c5a7610e6228aa', '187.226.73.237',
                '2806:104e:c:58f4:8514:c052:bed5:c83a')
            print(color('\n 🔴 Es importante que considere los siguientes parametros: 🔴', Colors.red))
            consult_api01.show_api01()
            key = input(f'\nIngrese la API key requerida por IpStack: \t')
            ip = input(f'\nIngrese la IP requerida por IpStack: \t')
            result01 = misfunciones.get_json_info_ipstack(ip, key)
            dicJSON01 = result01
            print(Fore.YELLOW)
            for clave, valor in dicJSON01.items():
                print(clave, ":", valor)
            print('\nFin llamado a la función número 1\n')
            print(f'Para la ejecución del programa se utilizo la API: {decision}\n')
        elif user_Decision == '2':
            decision = 'IpAPI'
            consult_api02 = miclase.Api02(
                '/json/', '/187.226.73.237', '/2806:104e:c:58f4:8514:c052:bed5:c83a')
            print(color('\n 🔴 Es importante que considere los siguientes parametros: 🔴', Colors.red))
            consult_api02.show_api02()
            ip2 = input(f'\nIngrese la IP requerida por IpAPI: \t')
            format0 = input(f'\nIngrese el formato requerido por IpAPI: \t')
            result02 = misfunciones.get_json_info_ipapi(ip2, format0)
            dicJSON02 = result02
            print(Fore.LIGHTCYAN_EX)
            for clave, valor in dicJSON02.items():
                print(clave, ":", valor)
            print('\nFin llamado a la función número 2\n')
            print(f'Para la ejecución del programa se utilizo la API: {decision}\n')
        elif user_Decision == '3':
            decision = 'Interrumpido'
            print('Software finalizado por el usuario ⛔')
            break
        else:
            decision = '\nOpción incorrecta 👻 intente de nuevo\n'
            print(decision)
    else:
        print('Ups algo terriblemente mal sucedio 🤓')


except Exception as e:
    print(e)


finally:
    print(color('\nFin del software 🏁\n', Colors.green))


Report01 = miclase.Report('Alan', 'Aplicación Informativa de direcciones IPv4 e IPv6 públicas.', '18/07/2021')
print(Fore.LIGHTMAGENTA_EX + 'Y un pequeño reporte 📋 ⬇' + '\n')
Report01.show_report()
misfunciones.clear_console()

