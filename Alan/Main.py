# Alejandro Alan Gutierrez Cortes, Jueves, 21/07/2021, Aplicación Informativa de direcciones IPv4 e IPv6 públicas.

import Def as df
import Model as mod
from colorit import *
from colorama import Fore, init
import pandas as pd


# * Inicializa imprimir en la consola a color
init()
init_colorit()


try:
    while not False:
        print(Fore.MAGENTA, '\n\t🛑 INFO IMPORTANTE 🛑')
        df.get_private_ip()
        df.get_public_ip()
        print(color('🍀 Inicio del software 🍀', Colors.red))
        print(Fore.BLUE)
        decision = None
        df.menu()
        user_Decision = input(f'\nIngrese una opción >>\t')
        if user_Decision == '1':
            decision = 'IpStack'
            consult_api01 = mod.Api01(
                '318ad030e610126d41c5a7610e6228aa', '187.226.73.237',
                '2806:104e:c:58f4:8514:c052:bed5:c83a')
            print(color('\n 🔴 Es importante que considere los siguientes parametros: 🔴', Colors.red))
            print(Fore.BLUE)
            consult_api01.show_api01()
            key = input(f'\nIngrese la API key requerida por IpStack: \t')
            ip = input(f'\nIngrese la IP requerida por IpStack: \t')
            result01 = df.get_json_info_ipstack(ip, key)
            dicJSON01 = result01
            #df01 = pd.DataFrame([[key, dicJSON01[key]] for key in dicJSON01.keys()], columns=['Clave', 'Valor'])
            #df01 = pd.DataFrame([[clave, dicJSON01[clave]] for clave, in dicJSON01.keys()], columns=['Clave', 'Valor'])
            df01 = pd.DataFrame([[clave, dicJSON01[clave]] for clave, valor in dicJSON01.items()], columns=['Clave', 'Valor'])
            print(f'\n{df01}')
            """
            dicJSON01 = result01
            print(Fore.YELLOW)
            for clave, valor in dicJSON01.items():
                print(clave, ":", valor))
            """
            print('\nFin llamado a la función número 1\n')
            print(f'Para la ejecución del programa se utilizo la API: {decision}')
        elif user_Decision == '2':
            decision = 'IpAPI'
            consult_api02 = mod.Api02(
                '/json/', '/187.226.73.237', '/2806:104e:c:58f4:8514:c052:bed5:c83a')
            print(color('\n 🔴 Es importante que considere los siguientes parametros: 🔴', Colors.red))
            print(Fore.LIGHTYELLOW_EX)
            consult_api02.show_api02()
            ip2 = input(f'\nIngrese la IP requerida por IpAPI: \t')
            format0 = input(f'\nIngrese el formato requerido por IpAPI: \t')
            result02 = df.get_json_info_ipapi(ip2, format0)
            dicJSON02 = result02
            #df02 = pd.DataFrame([[key, dicJSON02[key]] for key in dicJSON02.keys()], columns=['Clave', 'Valor'])
            #df02 = pd.DataFrame([[clave, dicJSON02[clave]] for clave, in dicJSON02.keys()], columns=['Clave', 'Valor'])
            df02 = pd.DataFrame([[clave, dicJSON02[clave]] for clave, valor in dicJSON02.items()], columns=['Clave','Valor'])
            print(f'\n{df02}')
            """
            dicJSON02 = result02
            print(Fore.LIGHTCYAN_EX)
            for clave, valor in dicJSON02.items():
                print(clave, ":", valor)
            """
            print('\nFin llamado a la función número 2\n')
            print(f'Para la ejecución del programa se utilizo la API: {decision}')
        elif user_Decision == '3':
            decision = 'Interrumpido'
            print('Software finalizado por el usuario ⛔')
            break
        else:
            error = '\nOpción incorrecta 👻 intente de nuevo'
            print(error)
    else:
        print('Ups algo terriblemente mal sucedio 🤓')


except Exception as e:
    print(f'\n{e} ❌')


finally:
    print(color('\nFin del software 🏁\n', Colors.green))


Report01 = mod.Report('Alan', 'Aplicación Informativa de direcciones IPv4 e IPv6 públicas.', df.get_time())
print(Fore.LIGHTMAGENTA_EX + 'Y un pequeño reporte 📋 ⬇' + '\n')
Report01.show_report()
df.clear_console()