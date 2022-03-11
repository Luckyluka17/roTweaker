from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo, showerror, showwarning
import os
import zipfile

window = tk.Tk()

def center_window2(width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

isloading=0

def download():
    global isloading
    if isloading == 0:
        if ch1.get() == 0 and ch2.get() == 0:
            showwarning("Erreur", "Veuillez séléctionner au moins 1 paquet à installer.")
        else:
            loading = ttk.Progressbar(
                length=230,
                value=0
            )
            loading.place(x=35, y=35)
            bouton.config(text="Annuler")
            check1.pack_forget()
            check2.pack_forget()
            texte1.config(text="Patientez")
            center_window2(300, 110)
            isloading = 1
            if ch2.get() == 1:
                texte1.config(text="Téléchargement de Python")
                loading.config(value=20)
                os.system('curl https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe --output "%TMP%\python-3.9.10.exe" && "%TMP%\python-3.9.10.exe" /silent >nul')
                os.system('pip install pypresence >nul')
            if ch1.get() == 1:
                texte1.config(text="Téléchargement de RoTweaker")
                os.system('curl https://codeload.github.com/Luckyluka17/roTweaker/zip/refs/heads/main -o rotweaker.zip >nul')
                with zipfile.ZipFile("rotweaker.zip","r") as zip_ref:
                    zip_ref.extractall("RoTweaker")
                os.system("del /F /Q rotweaker.zip")
                loading.config(value=50)
            texte1.config(text="Finalisation")
            loading.config(value=100)
            texte1.config(text="Terminé !")
            showinfo("Téléchargement terminé", "Un dossier c'est installé là où il y a ce fichier. Ouvrez le puis exécutez \"RoTweaker.exe\".\nEnjoy ;)")
            window.destroy()

            
            
    else:
        window.destroy()

window.title("Installateur de paquets")
center_window2(300, 135)
window.resizable(False, False)

ch1 = tk.IntVar()
ch2 = tk.IntVar()

texte1 = ttk.Label(
    text="Quel(s) paquet(s) souhaitez vous installer ?",
    font=("Calibri", 12)
)
texte1.pack()

check1 = ttk.Checkbutton(
    window,
    text="RoTweaker",
    variable=ch1,
    onvalue=1,
    offvalue=0
)
check1.pack()
check1.state(['!alternate'])

check2 = ttk.Checkbutton(
    window,
    text="Python",
    variable=ch2,
    onvalue=1,
    offvalue=0
)
check2.pack()
check2.state(['!alternate'])

ttk.Label(
    text=" "
).pack()

ttk.Label(
    text=" "
).pack()

bouton = ttk.Button(
    text="Démarrer l'installation",
    command=download
)
bouton.pack()
window.mainloop()