# Alejandro Alan Gutierrez Cortes, Mie, 21/07/2021, Aplicación Informativa de direcciones IPv4 e IPv6 públicas.

class Report:

    def __init__(self, n, c, f):
        self.author = n
        self.contents = c
        self.date = f

    def show_report(self):
        print('El software lo diseño: ' + self.author + '\n' + 'La actividad a realizar mediante el software es: ' +
              self.contents + '\n' 'Ultima modificación: ' + self.date)


class Api01:

    def __init__(self, a, b, c):
        self.api01_type1 = b
        self.api01_type2 = c
        self.api01_ty = a

    def show_api01(self):
        print(
            '\n' + 'La API Key pudiera ser de la siguiente manera: ' + self.api01_ty +
            '\n' + 'La red pudiera ser tipo IPv4: ' + self.api01_type1 +
            '\n' + 'La red pudiera ser tipo IPv6: ' + self.api01_type2)


class Api02:

    def __init__(self, a, b, c):
        self.api02_type1 = b
        self.api02_type2 = c
        self.api02_format = a

    def show_api02(self):
        print(
            '\n' + 'El formato para la consulta pudiera ser: ' + self.api02_format +
            '\n' + 'La red pudiera ser tipo IPv4: ' + self.api02_type1 +
            '\n' + 'La red pudiera ser tipo IPv6: ' + self.api02_type2)
