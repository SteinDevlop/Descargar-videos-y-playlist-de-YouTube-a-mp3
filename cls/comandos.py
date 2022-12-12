from cls.color import Colors as cl
from cls.mssj import msj
from pytube import Playlist
from pytube import YouTube
import moviepy.editor as mp
import os, shutil,time
import re
class commands:

    path_dowload = f"{os.getcwd()}\Download"
    path_playlist = f"{os.getcwd()}\download playlist"
    print(path_dowload)
    print(path_playlist)
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
        Titulo: {cl.UNDERLINE}{video.title}.{cl.END}
        Duracion: {cl.UNDERLINE}{video.length}{cl.END} Seg.
        Canal: {cl.UNDERLINE}{video.author}{cl.END}.
        """)
        print("".center(50,"-"))
        filter_video_audio = video.streams.filter(file_extension='mp4').first()
        try:
            video_mp4=filter_video_audio.download(cls.path_dowload)
        except Exception as e:
            print(f"Error: {type(e)}")
        msj.msj_download_finished()
        basePath, extension = os.path.splitext(video_mp4)
        with mp.VideoFileClip(os.path.join(basePath + ".mp4")) as clip:
            clip.audio.write_audiofile(os.path.join(basePath + ".mp3"))
        os.remove(os.path.join(basePath + ".mp4"))
        msj.msj_process_finished()
    @classmethod
    def playlist(cls,url):
        video_playlist=Playlist(url)
        print("Proceso de descarga".center(50,"-"))
        print("Informacion del video:")
        print(f"""
        Titulo: {cl.UNDERLINE}{video_playlist.title}{cl.END}.
        """)
        print("".center(50,"-"))
        confirm = str(input(f"Confirme la descarga con {cl.YELLOW}y{cl.END}: "))
        if confirm == "y":
            print("".center(50,"-"))
            print("Iniciando Descarga ...")
            for url in video_playlist:
                YouTube(url).streams.filter(only_audio=True).first().download(cls.path_playlist)
            msj.msj_download_finished()
            for file in os.listdir(cls.path_playlist):
                if re.search('mp4', file):
                    mp4_path = os.path.join(cls.path_playlist,file)
                    mp3_path = os.path.join(cls.path_playlist,os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)
            msj.msj_process_finished()
        elif confirm != "y":
            exit()