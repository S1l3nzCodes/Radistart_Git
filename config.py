#Configfile RadiStart
import webbrowser, sys, os, socket, time, getpass, subprocess
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


User=getpass.getuser()
Host=socket.gethostname()
print"User: "+User+"\n"+"Rechnername: "+Host
userpath = os.path.expanduser('~')
username = getpass.getuser()
Date=time.strftime("Datum: %d.%m.%Y")
Date2=time.strftime("%d.%m.%Y")


#Lokalisation
if str("Flo") in User:
    IP="http://192.168.2.200"
    print "zu Hause"
else:
    IP="http://172.24.105.118"
    print "bei der Arbeit"

aLogbuch=str("http://logbuch.uk-sh.de/logbuch/login.php?host=knrad017")
aLogbuchR=str("http://logbuch.uk-sh.de/logbuch/login.php")
aIntranet_Radiologie=str("http://10.253.53.23/Radiologie_Kiel/Intranet+_+Radiologie+Kiel+%28Passwortgesch%C3%BCtzt%29/Mitteilungen.html")
aIntranet=str("http://10.253.53.23/intranet.html")
aOP=str("http://172.24.181.10/OP-Plan/2013/Kalender/PerpetualCalendar21.htm")
aWebmail=str("https://webmail.uksh.de/CookieAuth.dll?GetLogon?curl=Z2Fowa&reason=0&formdir=1")
aSPX=str("http://10.253.53.224/webaspx/")
aBestellen=str("http://10.253.53.200:9911/einstieg.php")
aEssen=str("http://10.253.53.23/Intranet/Speisepl%C3%A4ne/Kiel+_+%C3%9Cbersicht+_+Speisepl%C3%A4ne+etc.html")
aQM=str("http://194.94.162.98/Roxtra/index.aspx")
aTelefonbuch=str(IP)
aRVPn=str(IP+"/RVPn")
aRVPa=str(IP+"/RVP")
aSPXa=str(IP+"/SPX")
aS1l3nz=str("http://github.com/S1l3nzCodes")
aTkMed=str("https://login.telekooperation-tnw.de")


#Logbuch Abfrage:
if str("CKNRR") in Host:
    print "Rechner ist Neuroradiologie"
    Logbuchadresse=aLogbuch
    Abteilung="Neuroradiologie"
elif str("RADPC801") in Host:
    print "Rechner ist Angio Neuro"
    Logbuchadresse=aLogbuch
    Abteilung="Neuroradiologie"
else:
    print "Rechner ist nicht Neuroradiologie"
    Logbuchadresse=aLogbuchR
    print Logbuchadresse
    Abteilung="Radiologie"



                        #Programme
Word='C:/Users/Public/Desktop/Microsoft Word 2010.lnk'
Excel='C:/Users/Public/Desktop/Microsoft Excel 2010.lnk'
Outlook='C:/Users/Public/Desktop/Microsoft Outlook 2010.lnk'
Dokumente='I:\Radiostart und Telefonliste\Dokumente'
OrbisFat="F:\orbis\dll\orbis.exe"
ImpaxEE="I:\Impax EE\Impaxee.exe"
OrbisRed='C:/Users/'+User+'/Desktop/ORBIS UKSH.lnk'

                        #Farben und Layout
hellblau="#AFBCE4"
dunkelblau="#6D87CF"
orange="#EFC58B"
gruen="#A3C08B"
grau="#BFBFBF"
dunkelgrau="#708090"

buttonfont="helvetica 13"
buttonfarbe=orange
schriftgross="helvetica 18"
schriftmittel="helvetica 16"

#Funktionen
def FLogbuch():
    webbrowser.open_new(Logbuchadresse)


def FBestellen():
    webbrowser.open_new(aBestellen)
               
def FIntranet():
    webbrowser.open_new(aIntranet)

def FIntranetR():
    webbrowser.open_new(aIntranet_Radiologie)

def FSPX():
    webbrowser.open_new(aSPX)

def FSpeiseplan():
    webbrowser.open_new(aEssen)

def TkMed():
    webbrowser.open_new(aTkMed)

def FS1l3nz():
    webbrowser.open_new(aS1l3nz)

    
def FNetzwerkfehler():
    print("Fehler! Das Netzwerklaufwerk wurde nicht gefunden.")


#Externe Programme:
def FOrbis():
    try:
        os.startfile(OrbisFat)
    except:
        try:
            os.startfile(OrbisRed)
        except:
            print "Kein Orbis :-("            
        log="Fehler", "AGFA ORBIS ist nicht installiert, oder der Sie sind nicht bei Citrix angemeldet."

def FImpax():
    try:
        os.startfile(ImpaxEE)
    except:
        print("Fehler! Impax ist nicht erreichbar")
        
def FEmail():
    try:
        os.startfile(Outlook)
    except:
        webbrowser.open(aWebmail)

def FWord():
    try:
        os.startfile(Word)
    except:
        print("Word ist nicht installiert")
        
def FExcel():
    try:
        os.startfile(Excel)
    except:
        print("Fehler", "Microsoft Excel ist nicht installiert.")
        
def FDoc():
    subprocess.Popen('explorer "I:\Radistart\Dokumente"')

def FRVP():
    webbrowser.open_new(aRVP)
    




def FRoxtra():
    webbrowser.open(aQM)

def FError():
    print("Fehler", "Diese Funktion ist noch in der Entwicklung...")
    

def Fueber():
    print("Informationen zu Radistart", " Das Programm ist noch im Betastadium \n \n Copyright by Florian Becker \n Fragen und Anregungen bitte per E-Mail an: \n S1l3nzCodes@googlemail.com \n Quellcodecode: https://github.com/S1l3nzCodes")

