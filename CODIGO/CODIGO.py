import tkinter as tk
from tkinter import filedialog
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def selecionar_pasta():
    folder = filedialog.askdirectory(title="SELECIONE O DIRETÓRIO DAS SUAS MÚSICAS!")
    entry_pasta.delete(0, tk.END)
    entry_pasta.insert(0, folder)

def obter_faixa(mp3_path):
    try:
        audio = EasyID3(mp3_path)
        track = audio.get("tracknumber", [None])[0]
        if track:
            return int(track.split("/")[0])
    except Exception:
        pass
    return 9999  

def renomear_musicas():
    folder = entry_pasta.get()
    name = entry_nome.get()

    arquivos = [f for f in os.listdir(folder) if f.lower().endswith('.mp3')]
    arquivos.sort(key=lambda x: obter_faixa(os.path.join(folder, x)))

    for count, file in enumerate(arquivos, start=1):
        old_path = os.path.join(folder, file)
        new_name = f"{name} {count:02d}{os.path.splitext(file)[1]}"
        os.rename(old_path, os.path.join(folder, new_name))

    label_status.config(text="Renomeação concluída!")

root = tk.Tk()
root.title("RENOMEAR MÚSICAS")

footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)
root.state('zoomed')

label_pasta = tk.Label(root, text="SELECIONE O DIRETÓRIO:")
label_pasta.pack()

entry_pasta = tk.Entry(root)
entry_pasta.pack()

button_pasta = tk.Button(root, text="SELECIONAR", command=selecionar_pasta)
button_pasta.pack()

label_nome = tk.Label(root, text="NOME UNIVERSAL:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

button_rename = tk.Button(root, text="RENOMEAR", command=renomear_musicas)
button_rename.pack()

label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()
