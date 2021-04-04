from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

with open("gooduni.csv", "r") as d:
    goodfile = d.read().splitlines()
with open('mails.csv') as f:
    brokenfile = f.read().splitlines()

fixxed = []

fixxedfile = open("fixedmails.csv", "a")
fixxedfile.truncate(0)

class Uni:
    def __init__(self, name, email):
        self.mail = email
        self.name = name

count = 0
for line in brokenfile:
    uni = ",".join(line.split(",")[:1])
    uni = uni[:-1][1:]
    mail = line.split(",")[len(line.split(","))-1]
    last = 0
    for i in goodfile:
        sim = similar(uni, i)
        if sim > last:
            fixxed.append(Uni(i, mail))
            last = sim
    count = count + 1

for repair in fixxed:
    fixxedfile.write(f"\"{repair.name}\",{repair.mail}\n")