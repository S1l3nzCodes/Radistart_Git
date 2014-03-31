#!C:/Python/python.exe
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        RadiStart
# Purpose:
#
# Author:      Florian Becker aka S1l3nz
#
# Created:     03.06.2013
# Last update: 26.11.2013 
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
import MySQLdb
import getpass

import config

User=getpass.getuser()
Host=socket.gethostname()
print"User: "+User+"\n"+"Rechnername: "+Host
userpath = os.path.expanduser('~')
username = getpass.getuser()

#Logbuch Abfrage:
if str("CKNRR") in Host:
    print "Rechner ist Neuroradiologie"
    Logbuchadresse=config.aLogbuch
    print Logbuchadresse
    Abteilung="Neuroradiologie"
elif str("RADPC801") in Host:
    print "Rechner ist Angio Neuro"
    Logbuchadresse=config.aLogbuch
    print Logbuchadresse
    Abteilung="Neuroradiologie"
else:
    print "Rechner ist nicht Neuroradiologie"
    Logbuchadresse=config.aLogbuchR
    print Logbuchadresse
    Abteilung="Radiologie"
    
#Externe Programme:
Orbis=os.path.join(userpath, 'Desktop', 'ORBIS UKSH.lnk')
Orbisfat="F:\orbis\dll\orbis.exe"

#Funktionen
def transport():
    webbrowser.open_new(Logbuchadresse)

def email():
    webbrowser.open_new(config.aWebmail)

def op():
    webbrowser.open_new(config.aOP)

def bestellen():
    webbrowser.open_new(config.aBestellen)
               
def intranet():
    webbrowser.open_new(config.aIntranet)

def intranet_Radiologie():
    webbrowser.open_new(config.aIntranet_Radiologie)

def spx():
    webbrowser.open_new(config.aSPX)

def essen():
    webbrowser.open_new(config.aEssen)


def Netwerkfehler():
    tkMessageBox.showerror \
                           ("Fehler! Das Netzwerklaufwerk wurde nicht gefunden.")


#Externe Programme:
def orbis():
    try:
        os.startfile(Orbis)
    except:
        tkMessageBox.showerror \
                           ("Fehler", "AGFA ORBIS ist nicht installiert, oder der Sie sind nicht bei Citrix angemeldet.")

def outlook():
    try:
        os.startfile(config.Outlook)
    except:
        webbrowser.open_new(config.aWebmail)

def word():
    try:
        os.startfile(config.Word)
    except:
        tkMessageBox.showerror \
                           ("Fehler", "Microsoft Word ist nicht installiert.")
        
def excel():
    try:
        os.startfile(config.Excel)
    except:
        tkMessageBox.showerror \
                           ("Fehler", "Microsoft Excel ist nicht installiert.")
        
def doks():
    #subprocess.Popen('explorer Dokumente')
    subprocess.Popen('explorer "I:\Radiostart und Telefonliste\Dokumente"')
    




def qm():
    webbrowser.open(config.aQM)

def error():
    tkMessageBox.showerror \
                           ("Fehler", "Diese Funktion ist noch in der Entwicklung...")
def ende():
    main.destroy()

def ueber():
    tkMessageBox.showinfo \
                           ("Informationen zu Radistart", " Das Programm ist noch im Betastadium \n \n Copyright by Florian Becker \n Fragen und Anregungen bitte per E-Mail an: \n S1l3nzCodes@googlemail.com \n Quellcodecode: https://github.com/S1l3nzCodes")
def send():
    #Wunsch=str(Entry_bestellwunsch.get()+"\t"+User)
    #Daten=open("Bestellwunsch.txt", "r")
    #Inhalt=Daten.read()
    #Daten.close
    #Daten=open("Bestellwunsch.txt", "w")
    #Neu=str(Inhalt + "\n" + Wunsch)
    #Daten.write(Neu)
    #Daten.close
    #Entry_bestellwunsch.delete(0, 99)
    tkMessageBox.showinfo \
                          ("Info", "Diese Funktion ist zur Zeit deaktiviert")

def send2():
    #Mecker=Entry_verbesserungswunsch.get()+"\t"+User                    #Unicode ascii??
    #Daten=open("Verbesserungen.txt", "r")
    #Inhalt=Daten.read()
    #Daten.close
    #Daten=open("Verbesserungen.txt", "w")
    #Neu=str(Inhalt + "\n" + Mecker+"\t"+"von: "+Host)
    #Daten.write(Neu)
    #Daten.close
    #Entry_verbesserungswunsch.delete(0, 99)
    tkMessageBox.showinfo \
                          ("Info", "Diese Funktion ist zur Zeit deaktiviert")
    
def bestellwunsch_anzeigen():
    #Daten=open("Bestellwunsch.txt", "r")
    #Inhalt=Daten.read()
    tkMessageBox.showinfo \
                          ("Bestellwunsch.txt", "Diese Funktion ist zur Zeit deaktiviert")

def verbesserungswunsch_anzeigen():
    #Daten=open("Verbesserungen.txt", "r")
    #Inhalt=Daten.read()
    tkMessageBox.showinfo \
                          ("Verbesserungen.txt", "Diese Funktion ist zur Zeit deaktiviert")

def telefon_suche():
    #Textbox.delete("end",11)
    connection = MySQLdb.connect (host = config.serverIP, user = "radistart", passwd = "radistart", db = "Telefonbuch")
    cursor = connection.cursor ()

    gesucht="'%"+str(Entry_Radiologietelefonbuch.get())+"%'"
    sql=("SELECT * FROM Telefonbuch WHERE name LIKE "+gesucht)
    print(sql)
    cursor.execute(sql)
    for i in cursor:
        I="Name:",i[0]," Nummer:",i[1], "Info:",i[2]," Fax: ",i[3]
        Textbox.insert("end",I)
        Textbox.insert("end","\n")

    connection.close()

def NeueSuche():
    Textbox.delete("1.0","end")
    Entry_Radiologietelefonbuch.delete(0,99)
    EntryDefault=tk.StringVar()

def bLesen():
        strBestellwunsch=str(eBestell.get())
        eBestell.delete(0,99)
        strAnzahl=str(eAnzahl.get())
        eAnzahl.delete(0,99)
        print (strBestellwunsch)+ " " +(strAnzahl)

def bWunsch():
    strWunsch=str(eWunsch.get())
    eWunsch.delete(0,99)
    print (strWunsch)+ " " +(User)
    

def bestellfenster():
    wBestellungen=tk.Tk()
    wBestellungen.title("Bestellwunsch eingeben:")
    fBestellungen=tk.Frame(wBestellungen, bg=hellblau)
    fBestellungen.pack()
    global wBestellungen
    lBestell=tk.Label(fBestellungen, text="Ware:", bg=hellblau, font=schriftgross)
    lBestell.grid(row=0, column=0)
    lAnzahl=tk.Label(fBestellungen, text="Anzahl:", bg=hellblau, font=schriftgross)
    lAnzahl.grid(row=0, column=1)
    eBestell=tk.Entry(fBestellungen, font=buttonfont, width=40)
    eBestell.grid(row=1, column=0)
    global eBestell
    eAnzahl=tk.Entry(fBestellungen, font=buttonfont, width=3)
    eAnzahl.grid(row=1, column=1)
    global eAnzahl
    BB=tk.Button(fBestellungen, text="Bestellwunsch abschicken", bg=buttonfarbe, font=buttonfont, command=error)
    BB.grid(row=1, column=3)

def wunschfenster():
    wwunsch=tk.Tk()
    wwunsch.title("Verbesserungswunsch eingeben:")
    global wwunsch
    fWunsch=tk.Frame(wwunsch, bg=hellblau)
    fWunsch.pack()
    lWunsch=tk.Label(fWunsch, text="Was könnte besser werden?:", font=buttonfont, bg=hellblau)
    lWunsch.grid(row
                 =0, column=0)
    eWunsch=tk.Entry(fWunsch, font=buttonfont, width=40)
    eWunsch.grid(row=1, column=0)
    global eWunsch
    BB=tk.Button(fWunsch, text="Verbesserungswunsch abschicken", font=buttonfont, command=error, bg=orange)
    BB.grid(row=1, column=3)





#GUI Layout
main=tk.Tk()
main.title('Radistart v0.4')
main.geometry('1200x700+20+20')
Hauptframe=tk.Frame(main, bd=1)
Hauptframe.pack(side="top",expand=1,fill="both")

#Spalten
Spalte_links=tk.Frame(Hauptframe, bd=2,bg=config.dunkelblau)
Spalte_links.pack(side="left",expand=1, fill="both")
Spalte_mitte=tk.Frame(Hauptframe, bd=2, bg=config.dunkelblau)
Spalte_mitte.pack(side="left", expand=1, fill="both")
Spalte_rechts=tk.Frame(Hauptframe, bd=2, bg=config.dunkelblau)
Spalte_rechts.pack(side="right",expand=1, fill="both")
Spalte_email=tk.Frame(Spalte_mitte, width=800, height=400)
Spalte_email.pack(expand=1, fill="both")

Spalte_info=tk.Frame(Spalte_rechts, bg=config.hellblau)
Spalte_info.pack(side="bottom",expand=1, fill="both")

Frame_telefon=tk.Frame(Spalte_mitte, bg=config.hellblau, bd=2, relief="raised")
Frame_telefon.pack(expand=1, fill="both")

Frame_telefon_Buttons=tk.Frame(Frame_telefon, bg=config.dunkelblau)
Frame_telefon_Buttons.pack(expand=1, fill="both", side="bottom")





#Buttons Links

#photo_intranet=tk.PhotoImage(file="Intranet.gif")
#Button_intranet=tk.Button(Spalte_links, image=photo_intranet, text="Intranet UKSH",font=buttonfont, command=intranet)
halberbutton=tk.Frame(Spalte_links)
halberbutton.pack(expand=1, fill="both")        #Frames für doppelbuttons
halberbutton2=tk.Frame(Spalte_links)
halberbutton2.pack(expand=1, fill="both")
                   
Button_intranet=tk.Button(halberbutton, text="Intranet UKSH", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=intranet)
Button_intranet.pack(expand=1,fill="both")

Button_Rad=tk.Button(halberbutton, text="Intranet Radiologie", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=intranet_Radiologie)
Button_Rad.pack(expand=1, fill="both")

Button_qm=tk.Button(Spalte_links, text="roXtra - QM", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=qm)
Button_qm.pack(expand=1, fill="both")

Button_spx=tk.Button(Spalte_links, text="SP-Expert", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=spx)
Button_spx.pack(expand=1, fill="both")

Button_logbuch=tk.Button(halberbutton2, text="Logbuch",font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=transport)
Button_logbuch.pack(expand=1,fill="both")

#Button_opplan=tk.Button(Spalte_links, text="OP-Plan", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=error)
#Button_opplan.pack(expand=1, fill="both")

Button_speiseplan=tk.Button(Spalte_links, text="Speiseplan", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=essen)
Button_speiseplan.pack(expand=1, fill="both")


#Buttons rechts
Button_Word=tk.Button(Spalte_rechts, text="Microsoft Word", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=word)
Button_Word.pack(expand=1, fill="both")

Button_Excel=tk.Button(Spalte_rechts, text="Microsoft Excel", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=excel)
Button_Excel.pack(expand=1, fill="both")

Button_Outlook=tk.Button(Spalte_rechts, text="Email / Webmail", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=outlook)
Button_Outlook.pack(expand=1, fill="both")

Button_Dokumente=tk.Button(Spalte_rechts, text="Dokumente", font=config.buttonfont, bg=config.buttonfarbe, bd=4, command=doks)
Button_Dokumente.pack(expand=1, fill="both")

Button_Bestellung=tk.Button(Spalte_rechts, text="Bestellwünsche", font=config.buttonfont, bg=config.buttonfarbe,bd=4, command=error)
Button_Bestellung.pack(expand=1, fill="both")

Button_Besprechung=tk.Button(Spalte_rechts, text="Besprechungswunsch", bg=config.buttonfarbe, font=config.buttonfont,bd=4, command=error)
Button_Besprechung.pack(expand=1, fill="both")

Button_Orbis=tk.Button(Spalte_rechts, text="Orbis", bg=config.buttonfarbe ,font=config.buttonfont,bd=4, command=orbis)
Button_Orbis.pack(expand=1, fill="both")


#Info
lt=time.localtime()
Datum=time.strftime("Datum: %d.%m.%Y", lt)
Zeit=time.strftime("Uhrzeit: %H. %M. %S", lt)

Label_datum=tk.Label(Spalte_info, text=Datum, font=config.schriftmittel, bg=config.hellblau)
Label_datum.pack(expand=1, fill="both")
    
Label_nutzer=tk.Label(Spalte_info, text="Benutzer: "+User+"\n"+"Rechnername: "+Host, font=config.buttonfont, bg=config.hellblau)
Label_nutzer.pack(expand=1, fill="both")

Label_Abteilung=tk.Label(Spalte_info, text=Abteilung, font=config.buttonfont, bg=config.hellblau)
Label_Abteilung.pack(expand=1, fill="both")




#Telefonbuch
SUCHE=tk.StringVar()        #für die Radiobuttons
SUCHE.set("Nach Namen suchen")
SucheDefault=tk.StringVar() #Defaultwert für das Nummer-Entry
SucheDefault.set("Nummer oder Namen eingeben...")

Label_Radiologietelefonbuch=tk.Label(Frame_telefon, font=config.schriftgross, text="Telefonbuch für die Radiologie", bg=config.hellblau)
Label_Radiologietelefonbuch.pack(expand=1, fill="x")
Frame_telefon2=tk.Frame(Frame_telefon,bd=4, bg=config.orange)
Frame_telefon2.pack(expand=1, fill="x")
Label_Suche=tk.Label(Frame_telefon2, font=config.buttonfont, text="Suchen: ", bg=config.orange)
Label_Suche.pack(side="left",expand=0, fill="x")
Entry_Radiologietelefonbuch=tk.Entry(Frame_telefon2, font=config.buttonfont)
Entry_Radiologietelefonbuch.pack(side="right",expand=1, fill="x")

Button_Radiologietelefonbuch=tk.Button(Frame_telefon_Buttons, font=config.buttonfont, text="Nummer suchen", command=telefon_suche, bg=config.buttonfarbe)
Button_Radiologietelefonbuch.pack(side="left",expand=1, fill="both")
Button_Radilogietelefonbuch_Neu=tk.Button(Frame_telefon_Buttons, font=config.buttonfont, text="Neue Suche", command=NeueSuche, bg=config.orange)
Button_Radilogietelefonbuch_Neu.pack(side="left",expand=1, fill="both")

Textbox=ScrolledText.ScrolledText(Frame_telefon, height=7, width=20, font=config.buttonfont)
Textbox.pack(expand=1, fill="x")



#Menueleiste
menue=tk.Menu(main)
mProg=tk.Menu(menue)
mProg.add_command(label="Beenden",command=ende)
mAbout=tk.Menu(menue)
mAbout.add_command(label="Über dieses Programm",command=ueber)
#mBestellung=tk.Menu(menue)
#mBestellung.add_command(label="Bestellliste anzeigen", command=bestellfenster)
#mBestellung.add_command(label="Bestelliste drucken", command=drucken_bestellwunsch)
#mBestellung.add_command(label="Bestellen", command=bestellen)
#mBestellung.add_command(label="Bestellwünsche löschen", command=bestellungloeschen)
#mVerbesserungen=tk.Menu(menue)
#mVerbesserungen.add_command(label="Verbesserungswünsche anzeigen", command=verbesserungswunsch_anzeigen)
#mVerbesserungen.add_command(label="Verbesserungswünsche drucken", command=drucken_verbesserungswunsch)
#mVerbesserungen.add_command(label="Verbesserungswüsnche löschen", command=verbesserungenloeschen)
menue.add_cascade(label="Programm", menu=mProg)
#menue.add_cascade(label="Bestellung", menu=mBestellung)
#menue.add_cascade(label="Verbesserungswünsche", menu=mVerbesserungen)
menue.add_cascade(label="Über", menu=mAbout)
main["menu"]=menue

#EMAIL PLatzhalter
Email_platzhalter=tk.Label(Spalte_email, font=config.buttonfont,height=20,width=60, bg=config.dunkelblau, text="Platzhalter...")
Email_platzhalter.pack(expand=1,fill="both")

main.mainloop()
