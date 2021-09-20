fileNameForReadingAndWriting = "2021.09.20"
openCsv = fileNameForReadingAndWriting + ".csv"
writeTxt = fileNameForReadingAndWriting + ".txt"

forrasfajl = open(openCsv, encoding="utf-8")

sorok = []

for sor in forrasfajl:
    sorok.append(sor.strip())

angolWord = []
magyarWord = []
szavak = []

for i in sorok:
    if "English" in i:
        szavak = i.split(",")
        angol = (szavak[2]).strip('"')
        magyar = (szavak[4]).strip('"')
        with open(writeTxt, "a", encoding='utf-8') as iras:
            iras.write(angol.lower())
            iras.write('#' + magyar.lower() + '\n')
        angolWord.append((szavak[2]).strip('"'))
        magyarWord.append((szavak[4]).strip('"'))
