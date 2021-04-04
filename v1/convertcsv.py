print("Start Converting...")

with open('mails.txt') as f:
    datei = f.read().splitlines()

csv = open("mails.csv", "a")
csv.truncate(0)
i = len(datei)
while i >= 2:
    uni = " ".join(datei[i-2].split(" ")[1:]).replace("f�r", "für")
    uni = uni.replace("Universit�t", "Universität")
    uni = uni.replace("Baden-W�rttemberg", "Baden-Württemberg")
    uni = uni.replace("W�rzburg", "Würzburg")
    uni = uni.replace("Saarbr�cken", "Saarbrücken")
    uni = uni.replace("Schw�bisch Gm�nd", "Schwäbisch Gmünd")
    uni = uni.replace("Wests�chsische", "Westsächsische")
    mail = " ".join(datei[i-1].split(" ")[2:]).replace("(at)", "@")
    csv.write(f"\"{uni}\",{mail}\n")
    i = i - 2

csv.close()
print("Converted File!")