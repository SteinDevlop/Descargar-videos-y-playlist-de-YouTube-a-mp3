from pytube import Playlist
from pytube import YouTube
import moviepy.editor as mp
import os, shutil,time
import re
class commands:
    path_dowload = "Descargar video de YT en mp3\Download"
    path_playlist = "Descargar video de YT en mp3\download playlist"
    def __init__(self) -> None:
        pass
    @classmethod
    def add_link(cls,url):
        with open(cls.path_list,"a",encoding="utf8") as lista:
            lista.write(url)
    @classmethod
    def one_link(cls,url):
        video = YouTube(url,use_oauth=False,allow_oauth_cache=True)
        video_title = video.title
        video_length = video.length
        video_author = video.author
        print("Proceso de descarga".center(50,"-"))
        print("Informacion del video:")
        print(f"""
        Titulo: {video.title}.
        Duracion: {video.length} Seg.
        Canal: {video.author}.
        """)
        print("".center(50,"-"))
        filter_video_audio = video.streams.filter(file_extension='mp4').first()
        try:
            video_mp4=filter_video_audio.download(cls.path_dowload)
        except Exception as e:
            print(f"Error: {type(e)}")
        print("""¡Descarga Finalizada!""")
        print("".center(50,"-"))
        print("Iniciando conversion de mp4 a mp3 ...")
        time.sleep(5)
        basePath, extension = os.path.splitext(video_mp4)
        with mp.VideoFileClip(os.path.join(basePath + ".mp4")) as clip:
            clip.audio.write_audiofile(os.path.join(basePath + ".mp3"))
        print("".center(50,"-"))
        print("¡Conversion finalizada!")
        print("".center(50,"-"))
        os.remove(os.path.join(basePath + ".mp4"))
        print("Proceso Finalizado")
        print("Volviendo al panel de opciones ...")
        print("".center(50,"-"))
        time.sleep(5)
    @classmethod
    def playlist(cls,url):
        video_playlist=Playlist(url)
        print("Proceso de descarga".center(50,"-"))
        print("Informacion del video:")
        print(f"""
        Titulo: {video_playlist.title}.
        """)
        print("".center(50,"-"))
        confirm = str(input("Confirme la descarga con y (diferente de y, cancelara la descarga): "))
        if confirm == "y":
            print("".center(50,"-"))
            print("Iniciando Descarga ...")
            for url in video_playlist:
                YouTube(url).streams.filter(only_audio=True).first().download(cls.path_playlist)
            print("¡Descarga finalizada!")
            print("".center(50,"-"))
            print("Iniciando conversion ...")
            for file in os.listdir(cls.path_playlist):
                if re.search('mp4', file):
                    mp4_path = os.path.join(cls.path_playlist,file)
                    mp3_path = os.path.join(cls.path_playlist,os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)
            print("Proceso Finalizado")
            print("Volviendo al panel de opciones ...")
            print("".center(50,"-"))
            time.sleep(5)
        elif confirm != "y":
            pass
    
    @classmethod
    def delete_data(cls):
        for filename in os.listdir(cls.path_dowload):
            file_path = os.path.join(cls.path_dowload, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Fallo Code: {e}")
        for filename in os.listdir(cls.path_playlist):
            file_path = os.path.join(cls.path_playlist, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Fallo Code: {e}")