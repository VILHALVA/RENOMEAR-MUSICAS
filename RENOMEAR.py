import tkinter as tk
from tkinter import filedialog
import os

def selecionar_pasta():
    folder = filedialog.askdirectory(title="Selecione o diretório da pasta de músicas")
    entry_pasta.delete(0, tk.END)
    entry_pasta.insert(0, folder)

def renomear_musicas():
    folder = entry_pasta.get()
    name = entry_nome.get()

    count = 1
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        new_name = f"{name} {count:02d}{os.path.splitext(file)[1]}"
        os.rename(file_path, os.path.join(folder, new_name))
        count += 1

    label_status.config(text="Renomeação concluída.")

root = tk.Tk()
root.title("Renomear Músicas")

label_pasta = tk.Label(root, text="Selecione o diretório da pasta de músicas:")
label_pasta.pack()

entry_pasta = tk.Entry(root)
entry_pasta.pack()

button_pasta = tk.Button(root, text="Selecionar pasta", command=selecionar_pasta)
button_pasta.pack()

label_nome = tk.Label(root, text="Digite o nome universal das músicas:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

button_rename = tk.Button(root, text="Renomear", command=renomear_musicas)
button_rename.pack()

label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()
