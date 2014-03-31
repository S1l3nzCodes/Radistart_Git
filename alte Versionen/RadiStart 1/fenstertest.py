#!C:/Python/python.exe
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Telefonnummern suche Radiologie
# Purpose:
#
# Author:      Florian Becker aka S1l3nz
#
# Created:     20.08.2013
# Copyright:   (c) S1l3nzCodes 2013         E-mail: S1l3nzCodes@googlemail.com
# Licence:     GPL v3
#-------------------------------------------------------------------------------
import Tkinter as tk
import ScrolledText
import tkMessageBox
import webbrowser
import os, socket, sys
import subprocess
from subprocess import call
import time
import sqlite3
import getpass

userpath = os.path.expanduser('~')
username = getpass.getuser()
filename = os.path.join(userpath, 'Desktop', 'IcoFX.lnk')
Filename="C:\Programme\IcoFX 1.6\IcoFX.exe"
Thunder="C:\Programme\Mozilla Thunderbird\thunderbird.exe"

print Filename
print filename
time.sleep(2)


def com():
    subprocess.call(["C:/Programme/Mozilla Thunderbird/thunderbird.exe"])
    
#Farben und schriftart:
hellblau="#AFBCE4"
dunkelblau="#6D87CF"
orange="#EFC58B"
gruen="#A3C08B"
buttonfont="helvetica 13"
buttonfarbe=orange
schriftgross="helvetica 18"
schriftmittel="helvetica 16"

main1=tk.Tk()
main1.title("Erstes Fenster")
b=tk.Button(main1, text="TEST", command=com)
b.pack()
main1.mainloop()
