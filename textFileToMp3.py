from gtts import gTTS
import os

mp3Filename = "2021_09_20.mp3"

fh = open("text.txt", encoding='utf-8')

sorok = []

for sor in fh:
    sorok.append(sor.strip())

text1 = list()
text2 = list()

for sor in sorok:
    szavak = sor.split("#")
    text1.append(szavak[0])
    text2.append(szavak[1])

with open(mp3Filename, 'wb') as fp:

    for t1, t2 in zip(text1, text2):
        t1 = str(t1)
        t2 = str(t2)
        print(t1 + " - " + t2)
        q = gTTS(text=t1, lang='en', slow=False)
        w = gTTS(text=t2, lang='hu', slow=False)
        q.write_to_fp(fp)
        w.write_to_fp(fp)

os.system(mp3Filename)
