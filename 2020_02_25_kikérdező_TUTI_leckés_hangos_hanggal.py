import stat
import time
from threading import Timer
from typing import Dict
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from termcolor import *

os.system('color')

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return  said

print()
print("Üdvözöllek az angol szótanító programunkban!")
print("Welcome to our English vocabulary program")
# speak("Welcome to our English vocabulary program")
print()
gyakorlas = True


while gyakorlas:

    hibak = {}
    hibak2 = {}


    def szotarkikerdezo_eredeti():
        print(100 * '\n')
        hibakSzama: int = 0

        for magyar, angol in szotar.items():

            print(magyar)

            timeout = 20
            t = Timer(timeout, print, [" Túl lassú! Csak 20 mp-ed van a válaszokra!\n"])
            t.start()

            valasz = get_audio()
            print(valasz)

            # valasz = input('angolul:')

            t.cancel()

            if valasz == angol:
                print('ok')
                speak(angol)
            while valasz != angol:


                print('nem jó\n')

                print(colored(magyar, 'red', 'on_white'), end='')
                print(colored('-', 'red', 'on_white'), end='')
                print(colored(angol, 'red', 'on_white'))
                print('\n')
                hibak[magyar] = angol
                speak(angol)
                valasz = get_audio()

        if hibak != {}:
            print(colored('Ezek voltak a hibás szavak: \n', 'red', 'on_white'))
            for magyar, angol in hibak.items():
                print(magyar, '-', angol)

            mehet = 0

            while mehet != 'i':
                mehet = input('Nyomj egy i-t ha mehet a kikérdezés!: ')

                if mehet == 'i':
                    print(100 * '\n')
                    os.chmod(hibagyujto, stat.S_IWRITE)
                    with open(hibagyujto, "a", encoding='utf-8') as iras:
                        for magyar, angol in hibak.items():

                            print(magyar)

                            valasz = get_audio()
                            print(valasz)

                            # valasz = input('angolul:')

                            if valasz == angol:
                                print('ok')
                                speak(angol)

                            while valasz != angol:
                                print('nem jó\n')
                                print(colored(magyar, 'red', 'on_white'), end='')
                                print(colored('-', 'red', 'on_white'), end='')
                                print(colored(angol, 'red', 'on_white'))
                                print('\n')
                                iras.write(magyar)
                                iras.write('-' + angol + '\n')
                                hibakSzama += 1
                                speak(angol)
                                valasz =get_audio()

                else:
                    print('Nem jó gombot nyomtál!')
        return hibakSzama


    def szotarkikerdezo_hibak():
        print(100 * '\n')
        hibakSzama: int = 0
        eltalaltSzavak = {}

        os.chmod(hibagyujto, stat.S_IWRITE)
        hibSzavakFile = open(hibagyujto, "r", encoding='utf-8')
        lista = hibSzavakFile.readlines()
        eltalaltSzavakFile = open(eltSzav, "r", encoding='utf-8')
        listaEltalalt = eltalaltSzavakFile.readlines()
        if len(listaEltalalt) > 0 and len(lista) > 0:
            y = 0
            while y != len(listaEltalalt):
                xdik = 0
                while xdik < len(lista):
                    if len(lista) > 0:
                        if listaEltalalt[y] in lista[xdik]:
                            lista.remove(lista[xdik])
                        xdik += 1
                y += 1
        if len(lista) == 0:
            print("Nincs kikérdeznivaló szó!")

        else:
            with open(hibagyujto, "w", encoding='utf-8') as ujraIras:
                ujraIras.writelines(lista)

            while True:
                inpHibSzam = input("Mennyi hibát akarsz gyakorolni? ")
                try:
                    inpHibSzam = int(inpHibSzam)
                    break
                except:
                    print("Nem jót írtál be!!!")

            with open(hibagyujto, "r", encoding='utf-8') as olvas:

                szotarak: Dict[str, str] = {}

                for fer in olvas:
                    xdik = fer.split("#")
                    adik = xdik[0]
                    bdik = xdik[1]
                    cdik = len(bdik) - 1
                    bdik = bdik[0:cdik]
                    szotarak[adik] = bdik
                    if len(szotarak) == inpHibSzam:
                        break
                # print(szotarak)

                for magyar, angol in szotarak.items():
                    print(magyar)

                    timeout = 20
                    t = Timer(timeout, print, [" Túl lassú! Csak 20 mp-ed van a válaszokra!\n"])
                    t.start()

                    valasz = get_audio()
                    print(valasz)

                    # valasz = input('angolul:')

                    t.cancel()

                    if valasz == angol:
                        print('ok')
                        eltalaltSzavak[magyar] = angol
                        speak(angol)
                    while valasz != angol:
                        print('nem jó\n')
                        print(colored(magyar, 'red', 'on_white'), end='')
                        print(colored('-', 'red', 'on_white'), end='')
                        print(colored(angol, 'red', 'on_white'))
                        print('\n')
                        hibak[magyar] = angol
                        hibakSzama += 1
                        speak(angol)
                        valasz = get_audio()

        # print(eltalaltSzavak)
        with open(eltSzav, "a", encoding='utf-8') as iras:
            for magyar, angol in eltalaltSzavak.items():
                iras.write(magyar)
                iras.write('-' + angol + '\n')
        return hibakSzama


    szemely = 0
    hibagyujto = None
    statik = None

    while szemely != 't' and szemely != 'b' and szemely != 'g' and szemely != 'l' and szemely != 'nb':
        print(colored('Figyelmeztetlek, hogy csak 20 mp-ed van a válaszokra!!!\n', 'red', 'on_white'))
        print(colored('I warn you, you only have 20 seconds to answer !!!\n', 'red', 'on_white'))
        szemely = input('Kit kell kikérdezni? Nyomd meg a megfelelő gombot! b-Bazsi, g-Gabi, t-Tomi, l-Lívia, nb-Nagy Balázs: \n'
                        'Who should be questioned? Press the appropriate button!: ')
        print()
        if szemely == 'b':
            eltSzav = "eltalaltSzavak_Bazsi.txt"
            statik = "Statisztika_Bazsi.txt"
            hibagyujto = 'hibák_Bazsi.txt'
        elif szemely == 't':
            eltSzav = "eltalaltSzavak_Tomi.txt"
            statik = "Statisztika_Tomi.txt"
            hibagyujto = 'hibák_Tomi.txt'
        elif szemely == 'g':
            eltSzav = "eltalaltSzavak_Gabi.txt"
            statik = "Statisztika_Gabi.txt"
            hibagyujto = 'hibák_Gabi.txt'
        elif szemely == 'l':
            eltSzav = "eltalaltSzavak_Livia.txt"
            statik = "Statisztika_Livia.txt"
            hibagyujto = 'hibák_Livia.txt'
        elif szemely == 'nb':
            eltSzav = "eltalaltSzavak_NBalazs.txt"
            statik = "Statisztika_NBalazs.txt"
            hibagyujto = 'hibák_NBalazs.txt'
        else:
            print('Nem jó gombot nyomtál!!!')

    forrasfajl = open("szótár.txt", encoding="utf-8")

    with open(statik, "r", encoding='utf-8') as stat_file:
        sorok = []
        gyakorolt_feleadatok = []
        for sor in stat_file:
            sorok.append(sor.strip())
        for i in sorok:
            if i[0] == "*":
                gyakorolt_feleadatok.append(i[1:])
    gyakorolt_feleadatok.sort()

    print("Ha a hibákat akarod gyakorolni nyomjál h-t! ")
    print("Ezeket gyakoroltad eddig: ", *gyakorolt_feleadatok)

    sorok = []

    for sor in forrasfajl:
        sorok.append(sor.strip())

    feladatok = []

    for i in sorok:
        if i[0] == "*":
            feladatok.append(i[1:])
    feladatok.append("h")
    feladatok.sort()
    print("Válassz feladatot:          ", end='')
    print(*feladatok)
    valasztas = ""
    valasztas = input()


    while not feladatok.count(valasztas):
        print()
        print("nem jó!")
        print()
        print("Válassz feladatot: ", end='')
        for i in feladatok:
            print(i, ", ", sep="", end="")
        # print(*feladatok)
        valasztas = input()

    if valasztas == "h":
        hibak_szama = szotarkikerdezo_hibak()


    szotar = {}

    for f in range(len(sorok) - 1):
        if sorok[f][1:] == valasztas:
            f += 1
            e = f
            for e in range(e, len(sorok) - 1):
                if sorok[e][0] == "*":
                    break
                x = sorok[e].split("#")
                a = x[0]
                b = x[1]
                c = len(b)
                b = b[0:c]
                szotar[a] = b

    if valasztas != "h":
        hibak_szama = szotarkikerdezo_eredeti()


    def statisztika(file):
        os.chmod(file, stat.S_IWRITE)
        with open(file, "a", encoding='utf-8') as iras:
            iras.write("*" + valasztas + "\nleckében" + " - " + str(
                hibak_szama) + " - " + " hiba volt - " + time.ctime() + "\n")
            os.chmod(file, stat.S_IREAD)


    statisztika(statik)

    os.chmod(hibagyujto, stat.S_IREAD)

    ujrakezdes = input("Akarsz még gyakorolni? i/n")

    while ujrakezdes != "i" or ujrakezdes != "n":
        if ujrakezdes == "i":
            gyakorlas = True
            break

        elif ujrakezdes == "n":
            gyakorlas = False
            print("Köszi, hogy gyakoroltál!")
            time.sleep(3.0)
            break
        else:
            print('Nem jó gombot nyomtál!!!')
            ujrakezdes = input("Akarsz még gyakorolni? i/n")
