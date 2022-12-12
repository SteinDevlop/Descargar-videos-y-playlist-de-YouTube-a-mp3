from cls.color import Colors as cl
import time
class msj:
    def msj_election():
        print("".center(50,"-"))
        print(f"Descargar video de {cl.RED}youtube{cl.END} en mp3")
        print("".center(50,"-"))
        print(f"""{cl.RED}Advertencia : No me hago responsable por el uso malintencionado del programa, es utilizado con propositos educativos.{cl.END}""")
        print("".center(50,"-"))
        print(f"""{cl.CYAN}1.{cl.END} Solo un video.
{cl.CYAN}2.{cl.END} Playlist.
{cl.CYAN}3.{cl.END} Salir.""")
        print("".center(50,"-"))
    def msj_download_finished():
        print(f"""{cl.YELLOW}¡Descarga Finalizada!{cl.END}""")
        print("".center(50,"-"))
        print(f"{cl.YELLOW}Iniciando conversion de mp4 a mp3 ...{cl.END}")
        print("".center(50,"-"))
        time.sleep(2)
    def msj_process_finished():
        print("".center(50,"-"))
        print(f"{cl.YELLOW}Proceso Finalizado{cl.END}")
        print(f"{cl.YELLOW}Volviendo al panel de opciones ...{cl.END}")
        print("".center(50,"-"))
        time.sleep(2)
