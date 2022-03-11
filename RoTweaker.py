import os, time, random
from tkinter import ttk
import tkinter as tk
from pypresence import Presence
import getpass, webbrowser
from tkinter.messagebox import showinfo, showerror, showwarning

appversion = "1.0.3"
os.system(f"title RoTweaker - Version {appversion}")

os.system("pip install pypresence")

def curl(link, file, extension):
    os.system(f"curl {link} -o {file}.{extension} >nul")

try:
    ID = '940908106379042846'
    RPC = Presence(ID)
    RPC.connect()
except:
    print("Discord n'a pas été detecté.")
        
def menu():
    try:
        RPC.update(
                state="Développé par Luckyluka17",
                details=f"{getpass.getuser()} utilise RoTweaker v{appversion}",
                large_image="large",
                buttons=[{"label": "Obtenir RoTweaker", "url": "https://luckyluka17.itch.io/rotweaker"}]
            )
    except:
        os.system("cls")
    os.system("cls")
    print("            **************************")
    print("            *  roTweaker for Roblox  *")
    print("            **************************")
    print(" ")
    print(" ")
    print(" ")
    print(" [1] Supprimer les textures     [2] Paramètres & infos")
    print(" [3] Obtenir le NewRoblox       [4] Débloquer les FPS")
    print(" [5] Réinstaller textures       [6] Supprimer les Tweaks")
    print(" ")
    try:
        ch=int(input(">"))
    except:
        os.system("cls")
        showerror("Erreur", "Entrez une valeur correcte (1, 2, etc...)")
        menu()
    
    if ch == 1:
        try:
            os.system(f'call "Scripts\\removetextures.bat"')
            showinfo("Textures supprimés", "Les textures ont bien été enlevés !")
        except:
            showerror("Erreur inconnu", "Une erreur est survenue lors de l'effacement des fichiers.")
        menu()
    elif ch == 2:
        try:
            RPC.update(
                state="Dans les Paramètres",
                details=f"{getpass.getuser()} utilise RoTweaker v1.0.2",
                large_image="large",
                large_text="Créé par Luckyluka17",
                buttons=[{"label": "Obtenir RoTweaker", "url": "https://luckyluka17.itch.io/rotweaker"}]
            )
        except:
            os.system("cls")
        os.system("cls")
        print("            **************************")
        print("            *    Paramètres & infos  *")
        print("            *   Créé par Luckyluka17 *")
        print("            **************************")
        print(" ")
        print(f"Répértoire de Roblox : C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Roblox\\")
        print(f"Version du jeu : {version}")
        print("")
        os.system("pause")
        menu()
    elif ch == 3:
        print("Lancement de Roblox...")
        os.system(f'"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Roblox\\Versions\\{version}\\RobloxPlayerBeta.exe" --app')
        menu()
    elif ch == 4:
        os.system(f'curl https://raw.githubusercontent.com/Luckyluka17/luckyluka17/main/rbxfpsunlocker.exe -o "C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Temp\\FPSUnlocker.exe" >nul')
        os.system(f'start "C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Temp\\FPSUnlocker.exe"')
        menu()
    elif ch == 5:
        try:
            os.system(f'call "Scripts\\restoretextures.bat"')
            showinfo("Textures restorées", "Toutes les textures de Roblox ont été remises !")
        except:
            showerror("Erreur inconnu", "Une erreur est survenue lors de l'éxécution d'un script.")
        menu()
    elif ch == 6:
        try:
            os.system(f'call "Scripts\\restoreall.bat"')
            showinfo("Paramètres restorés", "Tous les paramètres appliqués par l'application sur votre jeu ont été enlevés !")
        except:
            showerror("Erreur inconnu", "Une erreur est survenue lors de l'éxécution d'un script.")
        menu()


# Vérifier le dossier de Roblox (auto)
def verifydirectory():
    global version
    if os.path.exists(f'C:/Users/{getpass.getuser()}/AppData/Local/Roblox/Versions/{version}'):
        menu()
    else:
        showerror("Dossier Roblox non trouvé", "Le dossier de votre jeu n'a pas été trouvé. Soit il y a eu une mise à jour, soit vous ne l'avez pas installé. Veuillez entrer maneullement son nom dans la console.")
        version=input(f"Veuillez entrer la version de votre roblox (par exemple : {version}): ")
        verifydirectory()

# Version du jeu
curl("https://raw.githubusercontent.com/Luckyluka17/roTweaker/main/roversion.txt", "roversion", "txt")
curl("https://raw.githubusercontent.com/Luckyluka17/roTweaker/main/appversion.txt", "appversion", "txt")
with open("roversion.txt", "r") as f:
    version=f.readline(24)
    f.close()
with open("appversion.txt", "r") as f:
    appversionext=f.readline(5)
    f.close()
if appversionext == appversion:
    verifydirectory()
else:
    showwarning("Version de l'application", "Cette version de RoTweaker est obsolète, merci de le mettre à jour sur le site.")

print(getpass.getuser())