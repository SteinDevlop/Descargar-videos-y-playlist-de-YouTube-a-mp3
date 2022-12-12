from cls.comandos import commands as cm
from cls.mssj import msj
from cls.color import Colors as cl
eleccion_tipo = None
while eleccion_tipo != 4:
    msj.msj_election()
    try:
        eleccion_tipo = int(input(f"{cl.UNDERLINE}(1/2/3){cl.END}: "))
    except Exception as e:
        print(f"{cl.RED}Error encontrado tipo:{cl.END} {type(e)}")
    if eleccion_tipo == 1:
        try:
            print("".center(50,"-"))
            link = (str(input("Url del video YT: ")))
            cm.one_link(link)
            print("".center(50,"-"))
        except Exception as e:
            print(f"{cl.RED}Error encontrado tipo:{cl.END} {type(e)}")
            print("Volviendo a panel de opciones ...")
    elif eleccion_tipo == 2:
        try:
            print("".center(50,"-"))
            link = (str(input("Url de la playlist YT: ")))
            cm.playlist(link)
        except Exception as e:
            print(f"{cl.RED}Error encontrado tipo:{cl.END} {type(e)}")
            print("Volviendo a panel de opciones ...")
            print("".center(50,"-"))
    elif eleccion_tipo == 3:
        exit()