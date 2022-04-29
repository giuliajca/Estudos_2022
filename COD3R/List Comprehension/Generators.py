from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

screen = Tk()
title = screen.title('Baixe Músicas')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# FUNÇÃO PARA FAZER O DOWNLOAD VIA BOTÃO:
def download_file():
    pegar_link = link_field.get()
    # COM O PATH SELECIONADO:
    path_selecionado = path_label.cget("text")
    # DOWNLOAD DO VÍDEO:
    mp4_video = Youtube(pegar_link).streams.get_hightest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

# FUNÇÃO PARA SELECIONAR O CAMINHO PARA SALVAR
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

# LOGOTIPO: ADICIONANDO IMAGEM:
logo_img = PhotoImage(file='logotipo.png')
canvas.create_image(250, 80, image=logo_img)

# LINK FIELD:
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Cole o link do vídeo abaixo:', font=('Segoe Ui Light', 13))
canvas.create_window(250, 188, window=link_label)
canvas.create_window(250, 220, window=link_field)

# SELECIONAR O CAMINHO (PATH):
path_label = Label(screen, text='Quero salvar em (...)', font=('Segoe Ui Light', 13))
path_btn = Button(screen, text='Selecionar', command=select_path)
canvas.create_canvas.create_window(250,270, window=path_label)
window(250,300, window=path_btn)

# BOTÃO DOWNLOAD:
download_btn = Button(screen, text='Baixar Música', font=('Segoe Ui Light', 13))
canvas.create_window(250,370, window=download_btn)

# FUNÇÃO PARA ABRIR O PROGRAMA:
screen.mainloop()
